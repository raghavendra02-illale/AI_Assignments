marks = []

for i in range(10):
    mark = float(input(f"Enter mark for subject {i + 1}: "))
    marks.append(mark)

print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))
print("Average mark:", sum(marks) / len(marks))