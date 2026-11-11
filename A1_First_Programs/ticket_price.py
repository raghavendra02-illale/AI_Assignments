age = int(input("Enter your age: "))

# Example pricing rules; adjust if your trainer gave different slabs.
if age < 5:
    price = 0
elif age <= 12:
    price = 50
elif age <= 59:
    price = 100
else:
    price = 60

print("Ticket price: ₹", price)
