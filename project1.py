students = []

def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))
    students.append({"name": name, "marks": marks})
    print("Student added successfully.\n")


def display_students():
    if not students:
        print("No student records found.\n")
        return
    print("\nStudent Records:")
    for s in students:
        print(f"Name: {s['name']}, Marks: {s['marks']}")
    print()


def search_student():
    name = input("Enter student name to search: ")
    for s in students:
        if s["name"].lower() == name.lower():
            print(f"Student found: Name: {s['name']}, Marks: {s['marks']}\n")
            return
    print("Student not found.\n")


def delete_student():
    name = input("Enter student name to delete: ")
    for s in students:
        if s["name"].lower() == name.lower():
            students.remove(s)
            print("Student deleted successfully.\n")
            return
    print("Student not found.\n")


def sort_students():
    print("1. Sort by Name")
    print("2. Sort by Marks")
    choice = input("Enter choice: ")

    if choice == "1":
        students.sort(key=lambda x: x["name"].lower())
        print("Students sorted by name.\n")
    elif choice == "2":
        students.sort(key=lambda x: x["marks"])
        print("Students sorted by marks.\n")
    else:
        print("Invalid choice.\n")


def main():
    while True:
        print("Student Record Management System")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Sort Students")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            sort_students()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")


main()
