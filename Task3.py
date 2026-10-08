def calculate_total(price, quantity):
    return price * quantity

product = input("Enter product name: ")
price = int(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = calculate_total(price, quantity)

print("Product:", product)
print("Quantity:", quantity)
print("Final amount:", total)