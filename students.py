"""
Student Information System (Polished Version 2)
--------------------------------------------------
Adds: sorting (by name or age) and exporting a readable report file.
"""

FILENAME = "students.txt"
REPORT_FILENAME = "student_report.txt"

students = []


def load_students():
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                student = {
                    "id": int(parts[0]),
                    "name": parts[1],
                    "age": int(parts[2]),
                    "class": parts[3],
                    "guardian": parts[4],
                }
                students.append(student)
    except FileNotFoundError:
        pass


def save_students():
    with open(FILENAME, "w") as file:
        for student in students:
            line = f"{student['id']},{student['name']},{student['age']},{student['class']},{student['guardian']}\n"
            file.write(line)


def generate_new_id():
    if not students:
        return 1
    existing_ids = [student["id"] for student in students]
    return max(existing_ids) + 1


def get_valid_name(prompt):
    while True:
        name = input(prompt).strip()
        if name:
            return name
        print("Name cannot be blank. Please try again.")


def get_valid_age(prompt):
    while True:
        raw = input(prompt).strip()
        if raw.isdigit() and 3 <= int(raw) <= 25:
            return int(raw)
        print("Please enter a valid age (a whole number between 3 and 25).")


def get_valid_id(prompt):
    while True:
        raw = input(prompt).strip()
        if raw.isdigit():
            return int(raw)
        print("Please enter a valid numeric ID.")


def show_students(student_list=None):
    if student_list is None:
        student_list = students

    if not student_list:
        print("No students found.")
        return

    print(f"\n--- {len(student_list)} Student(s) ---")
    for student in student_list:
        print(
            f"ID: {student['id']} | Name: {student['name']} | "
            f"Age: {student['age']} | Class: {student['class']} | "
            f"Guardian: {student['guardian']}"
        )


def find_student_by_id(student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def add_student():
    name = get_valid_name("Enter student name: ")
    age = get_valid_age("Enter student age: ")
    student_class = get_valid_name("Enter student class (e.g. JSS2): ")
    guardian = get_valid_name("Enter guardian contact: ")

    new_student = {
        "id": generate_new_id(),
        "name": name,
        "age": age,
        "class": student_class,
        "guardian": guardian,
    }
    students.append(new_student)
    save_students()
    print(f"Added student: {new_student['name']} (ID: {new_student['id']})")


def search_student():
    student_id = get_valid_id("Enter student ID to search: ")
    student = find_student_by_id(student_id)
    if student:
        show_students([student])
    else:
        print("No student found with that ID.")


def update_student():
    student_id = get_valid_id("Enter student ID to update: ")
    student = find_student_by_id(student_id)
    if not student:
        print("No student found with that ID.")
        return

    print(f"Updating {student['name']}. Press Enter to keep the current value.")

    new_name = input(f"Name [{student['name']}]: ").strip()
    if new_name:
        student["name"] = new_name

    new_age = input(f"Age [{student['age']}]: ").strip()
    if new_age:
        if new_age.isdigit() and 3 <= int(new_age) <= 25:
            student["age"] = int(new_age)
        else:
            print("Invalid age — keeping the old value.")

    new_class = input(f"Class [{student['class']}]: ").strip()
    if new_class:
        student["class"] = new_class

    new_guardian = input(f"Guardian [{student['guardian']}]: ").strip()
    if new_guardian:
        student["guardian"] = new_guardian

    save_students()
    print("Student record updated.")


def delete_student():
    student_id = get_valid_id("Enter student ID to delete: ")
    student = find_student_by_id(student_id)
    if student:
        confirm = input(f"Delete {student['name']}? (y/n): ").strip().lower()
        if confirm == "y":
            students.remove(student)
            save_students()
            print(f"Deleted student: {student['name']}")
        else:
            print("Delete cancelled.")
    else:
        print("No student found with that ID.")


def filter_by_class():
    class_name = input("Enter class to filter by (e.g. JSS2): ").strip()
    matches = [s for s in students if s["class"].lower() == class_name.lower()]
    show_students(matches)


def sort_students():
    """Ask how to sort, then display students in that order (doesn't change storage order)."""
    print("Sort by: 1) Name  2) Age")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        sorted_list = sorted(students, key=lambda s: s["name"].lower())
    elif choice == "2":
        sorted_list = sorted(students, key=lambda s: s["age"])
    else:
        print("Invalid choice.")
        return

    show_students(sorted_list)


def export_report():
    """Write a readable report of all students to a text file."""
    if not students:
        print("No students to export.")
        return

    with open(REPORT_FILENAME, "w") as file:
        file.write("STUDENT REPORT\n")
        file.write("=" * 50 + "\n")
        file.write(f"Total students: {len(students)}\n\n")

        sorted_list = sorted(students, key=lambda s: s["name"].lower())
        for student in sorted_list:
            file.write(
                f"ID: {student['id']} | Name: {student['name']} | "
                f"Age: {student['age']} | Class: {student['class']} | "
                f"Guardian: {student['guardian']}\n"
            )

    print(f"Report exported to {REPORT_FILENAME}")


def main():
    load_students()

    while True:
        print(f"\n===== Student Information System ({len(students)} students) =====")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student by ID")
        print("4. Update student")
        print("5. Delete student")
        print("6. Filter by class")
        print("7. Sort students")
        print("8. Export report")
        print("9. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            filter_by_class()
        elif choice == "7":
            sort_students()
        elif choice == "8":
            export_report()
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
