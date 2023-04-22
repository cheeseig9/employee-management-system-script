import pymongo

# connect to the MongoDB database with network
client = pymongo.MongoClient("mongodb+srv://chetseig9:<password>@cluster0.3idaydz.mongodb.net/?retryWrites=true&w=majority")
db = client["employee_management"]
employees = db["employees"]

# initialize ID counter
id_counter = 0

# create employee
def create_employee():
    global id_counter
    name = input("Enter employee name: ")
    job = input("Enter employee job: ")
    salary = input("Enter employee salary: ")
    id_counter += 1
    employee = {"_id": id_counter, "name": name, "job": job, "salary": salary}
    result = employees.insert_one(employee)
    print("Employee added with ID:", id_counter)

# view employee
def view_employee():
    emp_id = int(input("Enter employee ID: "))
    employee = employees.find_one({"_id": emp_id})
    if employee:
        print("Employee details:")
        print("ID:", employee["_id"])
        print("Name:", employee["name"])
        print("Job:", employee["job"])
        print("Salary:", employee["salary"])
    else:
        print("Employee not found")

# edit employee
def edit_employee():
    emp_id = int(input("Enter employee ID to edit: "))
    employee = employees.find_one({"_id": emp_id})
    if employee:
        print("Employee details:")
        print("ID:", employee["_id"])
        print("Name:", employee["name"])
        print("Job:", employee["job"])
        print("Salary:", employee["salary"])
        confirm = input("Are you sure you want to edit this employee? (y/n): ")
        if confirm.lower() == "y":
            name = input("Enter new employee name: ")
            job = input("Enter new employee job: ")
            salary = input("Enter new employee salary: ")
            employees.update_one({"_id": emp_id}, {"$set": {"name": name, "job": job, "salary": salary}})
            print("Employee updated successfully")
    else:
        print("Employee not found")

# delete employee
def delete_employee():
    emp_id = int(input("Enter employee ID to delete: "))
    result = employees.delete_one({"_id": emp_id})
    if result.deleted_count == 1:
        print("Employee deleted successfully")
    else:
        print("Employee not found")

# main menu
while True:
    print("Employee Management System")
    print("1. Create Employee")
    print("2. View Employee")
    print("3. Edit Employee")
    print("4. Delete Employee")
    print("5. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        create_employee()
    elif choice == "2":
        view_employee()
    elif choice == "3":
        edit_employee()
    elif choice == "4":
        delete_employee()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
