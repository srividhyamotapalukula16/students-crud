from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.models import Student
from app.schemas import StudentCreate, StudentUpdate


def create_student(db: Session, student: StudentCreate):
    data = student.model_dump()

    db_student = Student(**data)

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


def get_students(
    db: Session,
    name=None,
    course=None,
    email=None,
    skip=0,
    limit=100
):
    query = db.query(Student)

    if name:
        query = query.filter(Student.name.ilike(f"%{name}%"))

    if course:
        query = query.filter(Student.course.ilike(f"%{course}%"))

    if email:
        query = query.filter(Student.email.ilike(f"%{email}%"))

    return query.offset(skip).limit(limit).all()


def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()


def update_student(
    db: Session,
    db_student: Student,
    student: StudentUpdate
):
    data = student.model_dump()

    for key, value in data.items():
        setattr(db_student, key, value)

    db.commit()
    db.refresh(db_student)

    return db_student


def patch_student(db: Session, db_student: Student, updates: dict):
    for key, value in updates.items():
        setattr(db_student, key, value)

    db.commit()
    db.refresh(db_student)

    return db_student


def delete_student(db: Session, db_student: Student):
    db.delete(db_student)
    db.commit()