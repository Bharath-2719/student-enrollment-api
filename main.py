from fastapi import FastAPI
import database

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "Student Course Enrollment Management API"
    }


@app.get("/enrollments")
def get_enrollments():

    return database.get_all_enrollments()


@app.get("/enrollments/{student_name}")
def search_enrollment(student_name: str):

    enrollment = database.search_enrollment(student_name)

    if enrollment:

        return enrollment

    return {
        "message": "Enrollment not found!"
    }


@app.post("/enrollments")
def add_enrollment(
    id: int,
    student_name: str,
    course_name: str,
    duration: str,
    fee: float,
    status: str
):

    database.insert_enrollment(
        id,
        student_name,
        course_name,
        duration,
        fee,
        status
    )

    return {
        "message": "Student enrolled successfully!"
    }


@app.delete("/enrollments/{student_name}")
def delete_enrollment(student_name: str):

    result = database.delete_enrollment(student_name)

    if result:

        return {
            "message": "Enrollment deleted successfully!"
        }

    return {
        "message": "Enrollment not found!"
    }


@app.put("/enrollments/{student_name}/status")
def update_status(
    student_name: str,
    new_status: str
):

    result = database.update_status(
        student_name,
        new_status
    )

    if result:

        return {
            "message": "Status updated successfully!"
        }

    return {
        "message": "Enrollment not found!"
    }
