

employees = {
    "E001": {"name": "Alice", "department": "Finance"},
    "E002": {"name": "Bob", "department": "IT"},
    "E003": {"name": "Charlie", "department": "HR"}
}


print(employees["E003"]['name'])



for emp in employees.values():
    print(emp['name'] , emp['department'])


for emp in employees:
    print(employees[emp]['name'] ,employees[emp]['department']  )