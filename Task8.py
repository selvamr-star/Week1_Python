try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a / b
    print("Result:", result)
except ValueError:
    print("Invalid input! Please enter numbers only.")
except ZeroDivisionError:
    print("Cannot divide by zero!")