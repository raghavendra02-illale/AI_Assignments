items = []

for i in range(5):
    item = input(f"Enter favourite item {i + 1}: ").strip()
    items.append(item)

print("Your favourite items:", items)