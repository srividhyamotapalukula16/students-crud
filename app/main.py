from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, HTTPException, Query, status
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app import models, crud
from app.schemas import StudentCreate, StudentUpdate, StudentPatch, StudentResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Students Database CRUD Application",
    description="Internship project using Python, FastAPI, and SQLite",
    version="1.0.0",
    lifespan=lifespan
)


@app.get("/")
def home():
    return {
        "message": "Welcome to the Students Database CRUD Application",
        "documentation": "/docs"
    }


@app.post(
    "/students",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    try:
        return crud.create_student(db, student)

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="A student with this email already exists."
        )

    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="A database error occurred."
        )


@app.get("/students", response_model=list[StudentResponse])
def read_students(
    name: str | None = None,
    course: str | None = None,
    email: str | None = None,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=100),
    db: Session = Depends(get_db)
):
    try:
        return crud.get_students(
            db,
            name=name,
            course=course,
            email=email,
            skip=skip,
            limit=limit
        )

    except SQLAlchemyError:
        raise HTTPException(
            status_code=500,
            detail="Could not retrieve students."
        )


@app.get("/students/{student_id}", response_model=StudentResponse)
def read_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = crud.get_student(db, student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found."
        )

    return student


@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    student: StudentUpdate,
    db: Session = Depends(get_db)
):
    db_student = crud.get_student(db, student_id)

    if db_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found."
        )

    try:
        return crud.update_student(db, db_student, student)

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="A student with this email already exists."
        )

    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Could not update student."
        )


@app.patch("/students/{student_id}", response_model=StudentResponse)
def patch_student(
    student_id: int,
    updates: StudentPatch,
    db: Session = Depends(get_db)
):
    db_student = crud.get_student(db, student_id)

    if db_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found."
        )

    changes = updates.model_dump(exclude_unset=True)

    if not changes:
        raise HTTPException(
            status_code=400,
            detail="Provide at least one field to update."
        )

    try:
        return crud.patch_student(db, db_student, changes)

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="A student with this email already exists."
        )

    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Could not update student."
        )


@app.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    db_student = crud.get_student(db, student_id)

    if db_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found."
        )

    try:
        crud.delete_student(db, db_student)

    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Could not delete student."
        )

    return None