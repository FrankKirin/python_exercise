
employee_info = { "John" : {"id": 12345, "department": "Human Resources"},
  "Sarah": {"id": 3, "department": "Software Engineering"},
  "Omar": {"id": 145, "department": "Marketing"}
}

# my code
employee_name = []

for name, detail in employee_info.items():
    employee_name.append(name)

print(employee_name)

# Internet code
import json

def find_names():
    data = json.load(employee_info)
    names = [name for name, details in data.items()]
    return names

print(find_names())