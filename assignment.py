class Employee:
    def _init_(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def _str_(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"

def sort_employee_data(employees, sort_parameter):
    if sort_parameter == 1:
        employees.sort(key=lambda emp: emp.age)
    elif sort_parameter == 2:
        employees.sort(key=lambda emp: emp.name)
    elif sort_parameter == 3:
        employees.sort(key=lambda emp: emp.salary)
    else:
        print("Invalid sorting parameter")
        return

    return employees

def main():
    employees = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000)
    ]

    print("Employee Table:")
    print("Employee ID  Name     Age  Salary (PM)")
    for emp in employees:
        print(emp)

    while True:
        try:
            sort_parameter = int(input("\nChoose a sorting parameter (1. Age, 2. Name, 3. Salary): "))
            sorted_employees = sort_employee_data(employees.copy(), sort_parameter)
            if sorted_employees:
                print("\nSorted Employee Table:")
                print("Employee ID  Name     Age  Salary (PM)")
                for emp in sorted_employees:
                    print(emp)
            break
        except ValueError:
            print("Invalid input. Please enter a valid sorting parameter.")

if _name_ == "_main_":
    main()