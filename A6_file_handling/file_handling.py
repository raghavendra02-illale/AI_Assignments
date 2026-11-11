100%
import csv
import json

names = ["Asha", "Ravi", "Mohan"]

# Text file: one name per line
with open("students.txt", "w", encoding="utf-8") as file:
    for name in names:
        file.write(name + "\n")

with open("students.txt", "r", encoding="utf-8") as file:
    print("Text file:", file.read())

# CSV file using DictWriter and DictReader
with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name"])
    writer.writeheader()
    for name in names:
        writer.writerow({"name": name})

with open("students.csv", "r", newline="", encoding="utf-8") as file:
    print("CSV file:", list(csv.DictReader(file)))

# JSON file using dump and load
student_data = {"students": names, "count": len(names)}
with open("students.json", "w", encoding="utf-8") as file:
    json.dump(student_data, file, indent=4)

with open("students.json", "r", encoding="utf-8") as file:
    print("JSON file:", json.load(file))