# Write to the file
file = open("students.txt", "w")
file.write("Anu, 85\n")
file.write("Ravi, 72\n")
file.write("Meena, 90\n")
    

# Read from the file
file = open("students.txt", "r")
content = file.read()
print(content)