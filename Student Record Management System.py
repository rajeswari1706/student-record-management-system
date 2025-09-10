# Student Record Management System
# By Raje

students = []

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    year = input("Enter Year: ")
    student = {"roll": roll, "name": name, "dept": dept, "year": year}
    students.append(student)
    print("✅ Student added successfully!\n")

def view_students():
    if not students:
        print("⚠️ No records found.\n")
        return
    print("\n--- Student Records ---")
    for s in students:
        print(f"Roll: {s['roll']} | Name: {s['name']} | Dept: {s['dept']} | Year: {s['year']}")
    print()

def search_student():
    roll = input("Enter Roll Number to search: ")
    for s in students:
        if s["roll"] == roll:
            print(f"✅ Found: Roll: {s['roll']} | Name: {s['name']} | Dept: {s['dept']} | Year: {s['year']}\n")
            return
    print("❌ Student not found!\n")

def update_student():
    roll = input("Enter Roll Number to update: ")
    for s in students:
        if s["roll"] == roll:
            print("Leave blank to keep old value.")
            name = input(f"Enter New Name ({s['name']}): ") or s['name']
            dept = input(f"Enter New Dept ({s['dept']}): ") or s['dept']
            year = input(f"Enter New Year ({s['year']}): ") or s['year']
            s.update({"name": name, "dept": dept, "year": year})
            print("✅ Record updated successfully!\n")
            return
    print("❌ Student not found!\n")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("✅ Student deleted successfully!\n")
            return
    print("❌ Student not found!\n")

def main():
    while True:
        print("===== Student Record Management =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("🚪 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
