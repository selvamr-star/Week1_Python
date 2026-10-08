students = [
    {"id": 1, "name": "Selva", "age": 22},
    {"id": 2, "name": "Suji", "age": 21},
    {"id": 3, "name": "Meena", "age": 19},
]

print("All students:")
for s in students:
    print(s["id"], s["name"], s["age"])

search_id = int(input("Enter student ID to search: "))

found = False
for s in students:
    if s["id"] == search_id:
        print("Found:", s["id"], s["name"], s["age"])
        found = True

if not found:
    print("No student with that ID")