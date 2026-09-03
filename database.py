enrollments = []


def insert_enrollment(id, student_name, course_name, duration, fee, status):

    enrollment = {
        "id": id,
        "student_name": student_name,
        "course_name": course_name,
        "duration": duration,
        "fee": fee,
        "status": status
    }

    enrollments.append(enrollment)

    print("Student enrolled successfully!")


def get_all_enrollments():

    return enrollments


def search_enrollment(student_name):

    for enrollment in enrollments:

        if enrollment["student_name"].lower() == student_name.lower():
            return enrollment

    return None


def delete_enrollment(student_name):

    for enrollment in enrollments:

        if enrollment["student_name"].lower() == student_name.lower():

            enrollments.remove(enrollment)

            print("Enrollment deleted successfully!")

            return True

    print("Enrollment not found!")

    return False


def update_status(student_name, new_status):

    enrollment = search_enrollment(student_name)

    if enrollment:

        enrollment["status"] = new_status

        print("Status updated successfully!")

        return True

    print("Enrollment not found!")

    return False
