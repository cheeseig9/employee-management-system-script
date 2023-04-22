import mysql.connector

# connect to the MySQL database
db = mysql.connector.connect(
    host="<host>",
    user="<username>",
    password="<password>",
    database="employee_management"
)
cursor = db.cursor()

# create employee table if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS employees (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), job VARCHAR(255), salary DECIMAL(10, 2))")

# create employee
def create_employee():
    name = input("Enter employee name: ")
    job = input("Enter employee job: ")
    salary = float(input("Enter employee salary: "))
    employee = (name, job, salary)
    sql = "INSERT INTO employees (name, job, salary) VALUES (%s, %s, %s)"
    cursor.execute(sql, employee)
    db.commit()
    print("Employee added with ID:", cursor.lastrowid)

# view employee
def view_employee():
    emp_id = int(input("Enter employee ID: "))
    sql = "SELECT * FROM employees WHERE id = %s"
    cursor.execute(sql, (emp_id,))
    employee = cursor.fetchone()
    if employee:
        print("Employee details:")
        print("ID:", employee[0])
        print("Name:", employee[1])
        print("Job:", employee[2])
        print("Salary:", employee[3])
    else:
        print("Employee not found")

# edit employee
def edit_employee():
    emp_id = int(input("Enter employee ID to edit: "))
    sql = "SELECT * FROM employees WHERE id = %s"
    cursor.execute(sql, (emp_id,))
    employee = cursor.fetchone()
    if employee:
        print("Employee details:")
        print("ID:", employee[0])
        print("Name:", employee[1])
        print("Job:", employee[2])
        print("Salary:", employee[3])
        confirm = input("Are you sure you want to edit this employee? (y/n): ")
        if confirm.lower() == "y":
            name = input("Enter new employee name: ")
            job = input("Enter new employee job: ")
            salary = float(input("Enter new employee salary: "))
            sql = "UPDATE employees SET name = %s, job = %s, salary = %s WHERE id = %s"
            cursor.execute(sql, (name, job, salary, emp_id))
            db.commit()
            print("Employee updated successfully")
    else:
        print("Employee not found")

# delete employee
def delete_employee():
    emp_id = int(input("Enter employee ID to delete: "))
    sql = "DELETE FROM employees WHERE id = %s"
    cursor.execute(sql, (emp_id,))
    db.commit()
    if cursor.rowcount == 1:
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

# close database connection
db.close()