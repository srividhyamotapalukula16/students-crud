from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_get_students():
    response = client.get("/students")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_student():
    student = {
        "name": "Test Student",
        "date_of_birth": "2005-05-15",
        "email": "teststudent@example.com",
        "phone": "9876543210",
        "course": "Computer Science",
        "address": "Hyderabad",
        "enrollment_date": "2026-10-12"
    }

    response = client.post("/students", json=student)

    assert response.status_code == 201
    assert response.json()["name"] == "Test Student"


def test_get_student_not_found():
    response = client.get("/students/999999")
    assert response.status_code == 404