import pickle

class Employee:
    def __init__(self, name, age, job_position):
        self.name = name
        self.age = age
        self.job_position = job_position

def create_employee():
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    job_position = input("Enter employee job position: ")
    return Employee(name, age, job_position)

def save_employees(employees, filename):
    with open(filename, 'wb') as file:
        pickle.dump(employees, file)

def load_employees(filename):
    with open(filename, 'rb') as file:
        employees = pickle.load(file)
    return employees


employees = []
employees.append(create_employee())
employees.append(create_employee())

filename = "employees.pickle"

save_employees(employees, filename)
loaded_employees = load_employees(filename)

for employee in loaded_employees:
    print("Name:", employee.name)
    print("Age:", employee.age)
    print("Job Position:", employee.job_position)
    print()
