import json

employees = [
    {"id": 1, "name": "Arun", "department": "IT"},
    {"id": 2, "name": "Divya", "department": "HR"},
    {"id": 3, "name": "Karthik", "department": "Finance"},
]

file = open("employees.json", "w")
json.dump(employees, file, indent=4)

file = open("employees.json", "r") 
data = json.load(file)

for emp in data:
    print(emp["name"], "-", emp["department"])