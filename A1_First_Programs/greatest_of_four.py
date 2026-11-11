numbers = []

for i in range(4):
    number = float(input(f"Enter number {i + 1}: "))
    numbers.append(number)

print("Greatest number:", max(numbers))