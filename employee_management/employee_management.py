import numpy as np
from tabulate import tabulate

FILENAME = 'employees.csv'

def create_file():
    # Create file with headers if it doesn't exist
    try:
        print("\nCouldn't find path to file, creating new...")
        with open(FILENAME, 'x') as file:
            file.write("ID,Name,Department,Age,Salary\n")
    except FileExistsError:
        pass  # File already exists
    
def load_employees():
    # Store employee data into key-value pairs ("dictionary")
    # and store those dictionaries into a list.
    employees = []
    try:
        with open(FILENAME, 'r') as file:
            # Read header
            headers = file.readline().strip().split(',')
            
            # Read employee data
            for line in file:
                if line.strip(): # Skip empty lines
                    values = line.strip().split(',')
                    employees.append({
                        'ID': int(values[0]),
                        'Name': values[1],
                        'Department': values[2],
                        'Age': int(values[3]),
                        'Salary': float(values[4])
                    })

    except FileNotFoundError:
        # Code to handle cases where file doesn't exist
        # Create file first, then load data
        # In essencee, this will return null, but still useful for creating an empty file
        create_file()
        load_employees()
    return employees        

def save_employee(new_employee):
    # Safety check to prevent writing empty dictionaries.
    if not new_employee:
        return
    
    # Write into file
    headers = new_employee.keys()
    values = [str(new_employee[field]) for field in headers]
    
    with open(FILENAME, 'a') as file:
        file.write(','.join(values) + '\n')

def add_employee():
    print("\n---- Add New Employee ----")
    
    # Get employee details from user.
    try:
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")
        age = int(input("Enter Age: "))
        salary = float(input("Enter Salary: "))
    except ValueError:
        print("Invalid input! Please enter correct data types.")
        return
    # Create new employee record
    new_employee = {
        'ID': emp_id,
        'Name': name,
        'Department': department,
        'Age': age,
        'Salary': salary
    }
    
    save_employee(new_employee)
    
    print(f"\nEmployee {name} added successfully!")
    
def view_employees():
    
    employees = load_employees()
    
    # Immediately quit the function if file is empty.
    if not employees:
        print("\nNo employee found in the system.")
        return
    
    print("\n---- All Employees ----")
    
    print(tabulate(employees, headers="keys", tablefmt="grid"))
    
def analyze_data():
    # Perform various data analysis on employee records
    
    # Immediately quit the function if data not exist.
    employees = load_employees()
    if not employees:
        print("No employees found for analysis.")
        return
    
    print("\n---- Data Analysis ----")
    
    # Extract salaries for NumPy operations
    salaries = np.array([float(emp['Salary']) for emp in employees])
    
    # Basic statistics
    total_employees = len(employees)
    avg_salary = np.mean(salaries)
    max_salary = np.max(salaries)
    min_salary = np.min(salaries)
    
    # Department counts
    dept_counts = {}
    for emp in employees:
        dept = emp['Department']
        dept_counts[dept] = dept_counts.get(dept, 0) + 1
    
    print(f"Total Employees: {total_employees}")
    print(f"Average Salary: {avg_salary:.2f}")
    print(f"Highest Salary: {max_salary}")
    print(f"Lowest Salary: {min_salary}")
    
    print("\nDepartment-wise Count:")
    for dept, count in dept_counts.items():
        print(f"{dept:<15} {count}")

def show_menu():
    # Display main menu and handle user choices.
    while True:
        print("\n==== Employee Management System ====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Analyze Data")
        print("4. Exit")

        try:
            choice = input("\nEnter your choice (1-4): ")
            if choice == '1':
                add_employee()
            elif choice == '2':
                view_employees()
            elif choice == '3':
                analyze_data()
            elif choice == '4':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice! Please enter a number between 1-4.")
        except KeyboardInterrupt: # handle cases like terminating program with Ctrl + C
            print("\nTerminating execution of the program.")
            break
        
def main():
    # Main function to run the employee management system
    print("====== Employee Record Management System with Analysis ======")
    create_file() 
    show_menu()

if __name__ == "__main__":
    main()
