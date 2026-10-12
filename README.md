\# Students Database CRUD Application



\## Project Overview



The Students Database CRUD Application is a backend application developed using Python, FastAPI, and SQLite. It manages student information through REST API endpoints.



\## Objectives



\* Store student information in a database.

\* Create, retrieve, update, and delete student records.

\* Validate student details.

\* Provide API documentation for easy testing.



\## Technologies Used



\* Python

\* FastAPI

\* SQLite

\* SQLAlchemy

\* Pydantic

\* Pytest



\## Features



\* Add new students.

\* View all student records.

\* Search students by name, course, or email.

\* Retrieve an individual student by ID.

\* Update student details.

\* Delete student records.

\* Validate email addresses and required fields.

\* Automatically generate API documentation.



\## Student Information



The application supports the following fields:



\* Student ID

\* Name

\* Date of Birth

\* Email

\* Phone Number

\* Course

\* Address

\* Enrollment Date



\## Installation and Setup



\### 1. Clone the repository



Clone the project from GitHub after uploading it.



\### 2. Create a virtual environment



```bash

python -m venv venv

```



\### 3. Activate the virtual environment on Windows



```cmd

venv\\Scripts\\activate

```



\### 4. Install dependencies



```bash

pip install -r requirements.txt

```



\### 5. Start the application



```bash

uvicorn app.main:app --reload

```



\### 6. Open API documentation



Visit http://127.0.0.1:8000/docs in your browser.



\## Running Tests



Run the automated tests using:



```bash

python -m pytest -v

```



\## API Endpoints



| Method | Endpoint                 | Purpose                  |

| ------ | ------------------------ | ------------------------ |

| GET    | `/`                      | Welcome message          |

| POST   | `/students`              | Create a student         |

| GET    | `/students`              | Retrieve student records |

| GET    | `/students/{student\_id}` | Retrieve a student by ID |

| PUT    | `/students/{student\_id}` | Replace student details  |

| PATCH  | `/students/{student\_id}` | Update selected fields   |

| DELETE | `/students/{student\_id}` | Delete a student         |



\## Database



The application uses SQLite to store student records. The database file is created automatically when the application starts.



\## Conclusion



This project demonstrates REST API development, database integration, data validation, CRUD operations, and automated testing using Python.



