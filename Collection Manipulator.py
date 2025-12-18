print("Welcome to the Student Data Organizer!")

students = []         
student_data = {}      

while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print("\nEnter student details:")
            sid = int(input("Student ID: "))
            name = input("Name: ")
            age = int(input("Age: "))
            grade = input("Grade: ")
            dob = input("Date of Birth (DD-MM-YYYY): ")

            subjects_input = input("Subjects (comma-separated): ")
            subjects = subjects_input.split(",")

            immutable_info = (sid, dob)   

            student_record = {
                "info": immutable_info,
                "name": name,
                "age": age,
                "grade": grade,
                "subjects": subjects
            }

            students.append(student_record)
            student_data[sid] = student_record

            print("Student added successfully!")

        case 2:
            print("\n--- Display All Students ---")
            if not students:
                print("No student records found.")
            else:
                for s in students:
                    print(
                        f"Student ID: {s['info'][0]} | "
                        f"Name: {s['name']} | "
                        f"Age: {s['age']} | "
                        f"Grade: {s['grade']} | "
                        f"Subjects: {', '.join(s['subjects'])}"
                    )

        case 3:
            sid = int(input("\nEnter Student ID to update: "))
            if sid in student_data:
                print("1. Update Age")
                print("2. Update Subjects")
                update_choice = int(input("Enter choice: "))

                match update_choice:
                    case 1:
                        new_age = int(input("Enter new age: "))
                        student_data[sid]["age"] = new_age
                        print("Age updated successfully!")

                    case 2:
                        new_subjects = input("Enter new subjects (comma-separated): ")
                        student_data[sid]["subjects"] = new_subjects.split(",")
                        print("Subjects updated successfully!")

                    case _:
                        print("Invalid update option.")
            else:
                print("Student ID not found.")

        case 4:
            sid = int(input("\nEnter Student ID to delete: "))
            if sid in student_data:
                del student_data[sid]
                for i in range(len(students)):
                    if students[i]["info"][0] == sid:
                        del students[i]
                        break
                print("Student deleted successfully!")
            else:
                print("Student ID not found.")

        case 5:
            subject_set = set()
            for s in students:
                for sub in s["subjects"]:
                    subject_set.add(sub.strip())

            print("\n--- Subjects Offered ---")
            for subject in subject_set:
                print(subject)

        case 6:
            print("\nThank you for using the Student Data Organizer!")
            break

        case _:
            print("Invalid choice. Please try again.")