#!/bin/bash

# Load the MySQL password from a separate file
password=$(<password.txt)

# Configuration for the MySQL connection
user="<username>"
host="<host>"
database="<database>"
port="3306"

# Function to create employee
create_employee() {
    read -p "Enter employee name: " name
    read -p "Enter employee job: " job
    read -p "Enter employee salary: " salary
    mysql -u$user -p$password -h$host -P$port $database -e "INSERT INTO employees (name, job, salary) VALUES ('$name', '$job', '$salary')"
    echo "Employee created"
}

# Function to view employee
view_employee() {
    read -p "Enter employee ID: " id
    employee=$(mysql -u$user -p$password -h$host -P$port $database -se "SELECT name, job, salary FROM employees WHERE id = $id")
    if [[ -n "$employee" ]]; then
        echo "$employee"
    else
        echo "Employee not found"
    fi
}

# Function to edit employee
edit_employee() {
    read -p "Enter employee ID: " id
    employee=$(mysql -u$user -p$password -h$host -P$port $database -se "SELECT name, job, salary FROM employees WHERE id = $id")
    if [[ -n "$employee" ]]; then
        echo "Employee found:"
        echo "$employee"
        read -p "Do you want to edit this employee? (Y/N): " confirm
        if [[ "$confirm" == "Y" || "$confirm" == "y" ]]; then
            read -p "Enter new name (leave blank to keep current): " name
            read -p "Enter new job (leave blank to keep current): " job
            read -p "Enter new salary (leave blank to keep current): " salary
            query="UPDATE employees SET"
            if [[ -n "$name" ]]; then
                query+=" name='$name',"
            fi
            if [[ -n "$job" ]]; then
                query+=" job='$job',"
            fi
            if [[ -n "$salary" ]]; then
                query+=" salary='$salary',"
            fi
            query=${query%,}" WHERE id = $id"
            mysql -u$user -p$password -h$host -P$port $database -e "$query"
            echo "Employee updated"
        fi
    else
        echo "Employee not found"
    fi
}

# Function to delete employee
delete_employee() {
    read -p "Enter employee ID: " id
    employee=$(mysql -u$user -p$password -h$host -P$port $database -se "SELECT name, job, salary FROM employees WHERE id = $id")
    if [[ -n "$employee" ]]; then
        echo "Employee found:"
        echo "$employee"
        read -p "Do you want to delete this employee? (Y/N): " confirm
        if [[ "$confirm" == "Y" || "$confirm" == "y" ]]; then
            mysql -u$user -p$password -h$host -P$port $database -e "DELETE FROM employees WHERE id = $id"
            echo "Employee deleted"
        fi
    else
        echo "Employee not found"
    fi
}

# Main program loop
while true; do
    echo "Employee Management System"
    echo "1. Create Employee"
    echo "2. View Employee"
    echo "3. Edit Employee"
    echo "4. Delete Employee"
    echo "5. Exit"
    read -p "Enter your choice: " choice
    case "$choice" in
        1) create_employee ;;
        2) view_employee ;;
        3) edit_employee ;;
        4) delete_employee ;;
        5) break ;;
        *) echo "Invalid choice" ;;
    esac
done