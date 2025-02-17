from flask import Flask, request

app = Flask(__name__)

employees = {}

class Employee:
    existing_emp_ids = set()
    
    def __init__(self, employee_id, name, department):
        if employee_id in Employee.existing_emp_ids:
            raise ValueError("Employee ID must be unique.")
        
        self.employee_id = employee_id
        self.employee_name = name
        self.employee_dept = department
        Employee.existing_emp_ids.add(employee_id)
    
    def display_employee(self):
        return f"ID: {self.employee_id}, Name: {self.employee_name}, Department: {self.employee_dept}"

@app.route('/')
def home():
    return "Welcome to Employee Management System"

@app.route('/add_employee')
def add_employee():
    try:
        employee_id = int(request.args.get('employee_id'))
        name = request.args.get('name')
        department = request.args.get('department')
        
        if not all([employee_id, name, department]):
            return "Missing parameters! Please provide employee_id, name, and department."
        
        employee = Employee(employee_id, name, department)
        employees[employee_id] = employee
        return f"Employee added: {employee.display_employee()}<br><br>All Employees:<br>" + "<br>".join(emp.display_employee() for emp in employees.values())
    
    except ValueError as e:
        return str(e)
    
    except Exception:
        return "Invalid input. Please check your parameters."

if __name__ == '__main__':
    app.run(debug=True)
