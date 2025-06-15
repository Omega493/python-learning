# Employee Management System with Data Analysis

A command-line based Employee Management System written in **Python**, featuring data entry, record viewing, and insightful salary analysis using **NumPy** and **Tabulate**.

---

## 📋 Features

- Add new employees with structured input
- View all employee records in a neat table format
- Analyze employee data:
  - Total number of employees
  - Average, highest, and lowest salaries
  - Department-wise employee count
- Data stored persistently in a CSV file
- Handles file creation and user input validation
- KeyboardInterrupt-safe (e.g., Ctrl+C won’t crash the program)

---

## Technologies Used

- `Python 3.13+`
- [`NumPy`](https://numpy.org/) – for numerical operations
- [`Tabulate`](https://pypi.org/project/tabulate/) – for pretty terminal tables
- CSV file handling with Python’s built-in `open()` function

---

## 🛠️ Setup Instructions

1. **Clone or download the repository**
   ```bash
   git clone https://github.com/Omega493/python-learning.git
   cd python-learning/employee_management
   ```

2. **Install dependencies**

   ```bash
   pip install numpy tabulate
   ```

3. **Run the application**

   ```bash
   python employee_management.py
   ```

---

## 🗃️ Data Format

Data is stored in a file named `employees.csv` with the following structure:

```
ID,Name,Department,Age,Salary
101,Alice,HR,28,50000.0
102,Bob,IT,35,80000.0
...
```

Each record is appended to this file when a new employee is added.

---

## 📈 Sample Output

```
==== Employee Management System ====

List of available options:-
1. Add Employee
2. View All Employees
3. Analyze Data
4. Exit
```

Viewing employee records:

```
+-----+--------+-------------+-----+----------+
| ID  | Name   | Department  | Age | Salary   |
+-----+--------+-------------+-----+----------+
| 101 | Alice  | HR          | 28  | 50000.0  |
| 102 | Bob    | IT          | 35  | 80000.0  |
+-----+--------+-------------+-----+----------+
```

---
