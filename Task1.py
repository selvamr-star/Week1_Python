name=input("Enter student name:")
mark1=int(input("Enter mark 1:"))
mark2=int(input("Enter mark 2:"))
mark3=int(input("Enter mark 3:"))

tot = mark1+mark2+mark3
avg = tot/3

print("Name:",name)
print("Total:",tot)
print("Avereage:",avg)

if avg >= 50:
    print("Result: pass")

else:
    print("Result: fail")