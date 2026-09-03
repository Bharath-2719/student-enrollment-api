import database


USER_CHOICE = """
Enter:

- 'a' to add a new student enrollment
- 'l' to list all enrollments
- 's' to search for a student
- 'd' to delete enrollment
- 'u' to update enrollment status
- 'q' to quit

Your choice: """


# Add Enrollment
def prompt_add_enrollment():

    id = int(input("Enter enrollment id: "))
    student_name = input("Enter student name: ")
    course_name = input("Enter course name: ")
    duration = input("Enter course duration: ")
    fee = float(input("Enter course fee: "))
    status = input("Enter enrollment status: ")

    database.insert_enrollment(
        id,
        student_name,
        course_name,
        duration,
        fee,
        status
    )


# List Enrollments
def list_enrollments():

    enrollments = database.get_all_enrollments()

    for enrollment in enrollments:

        print(
            f"ID: {enrollment['id']} "
            f"| Student: {enrollment['student_name']} "
            f"| Course: {enrollment['course_name']} "
            f"| Duration: {enrollment['duration']} "
            f"| Fee: ₹{enrollment['fee']} "
            f"| Status: {enrollment['status']}"
        )


# Search Enrollment
def prompt_search_enrollment():

    student_name = input("Enter student name: ")

    enrollment = database.search_enrollment(student_name)

    if enrollment:

        print("\nEnrollment Found!")

        print(f"ID       : {enrollment['id']}")
        print(f"Student  : {enrollment['student_name']}")
        print(f"Course   : {enrollment['course_name']}")
        print(f"Duration : {enrollment['duration']}")
        print(f"Fee      : ₹{enrollment['fee']}")
        print(f"Status   : {enrollment['status']}")

    else:

        print("Enrollment not found!")


# Delete Enrollment
def prompt_delete_enrollment():

    student_name = input("Enter student name to delete: ")

    database.delete_enrollment(student_name)


# Update Status
def prompt_update_status():

    student_name = input("Enter student name: ")
    new_status = input("Enter new status: ")

    database.update_status(
        student_name,
        new_status
    )


def menu():

    user_input = input(USER_CHOICE)

    while user_input != "q":

        if user_input == "a":
            prompt_add_enrollment()

        elif user_input == "l":
            list_enrollments()

        elif user_input == "s":
            prompt_search_enrollment()

        elif user_input == "d":
            prompt_delete_enrollment()

        elif user_input == "u":
            prompt_update_status()

        else:
            print("Invalid choice!")

        user_input = input(USER_CHOICE)


menu()
