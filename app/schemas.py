from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class StudentCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    date_of_birth: date
    email: EmailStr
    phone: str = Field(min_length=1, max_length=20)
    course: Optional[str] = None
    address: Optional[str] = None
    enrollment_date: Optional[date] = None


class StudentUpdate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    date_of_birth: date
    email: EmailStr
    phone: str = Field(min_length=1, max_length=20)
    course: Optional[str] = None
    address: Optional[str] = None
    enrollment_date: Optional[date] = None


class StudentPatch(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=100)
    date_of_birth: Optional[date] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(default=None, min_length=1, max_length=20)
    course: Optional[str] = None
    address: Optional[str] = None
    enrollment_date: Optional[date] = None


class StudentResponse(BaseModel):
    id: int
    name: str
    date_of_birth: date
    email: EmailStr
    phone: str
    course: Optional[str] = None
    address: Optional[str] = None
    enrollment_date: Optional[date] = None

    model_config = ConfigDict(from_attributes=True)