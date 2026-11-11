
import csv
import json


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = 0
        self.update_marks(marks)

    def update_marks(self, marks):
        if not isinstance(marks, (int, float)) or marks < 0 or marks > 100:
            raise ValueError("Please enter marks between 0 and 100.")
        self.__marks = marks

    def show_marks(self):
        return self.__marks

    def calculate_grade(self):
        if self.__marks >= 90:
            return "A"
        elif self.__marks >= 75:
            return "B"
        elif self.__marks >= 60:
            return "C"
        elif self.__marks >= 40:
            return "D"
        else:
            return "F"

    def __str__(self):
        return f"Student: {self.name}, Marks: {self.__marks}, Grade: {self.calculate_grade()}"

    def get_details(self):
        return {
            "name": self.name,
            "marks": self.__marks,
            "grade": self.calculate_grade()
        }


def save_student_data(student_list):

    with open("students.txt", "w", encoding="utf-8") as file:
        for student in student_list:
            file.write(str(student) + "\n")

    with open("students.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "marks", "grade"])
        writer.writeheader()

        for student in student_list:
            writer.writerow(student.get_details())

    with open("students.json", "w", encoding="utf-8") as file:
        data = [student.get_details() for student in student_list]
        json.dump(data, file, indent=4)


def check_marks_file(file_name):

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for number, line in enumerate(file, start=1):
                marks = line.strip()

                if marks == "":
                    continue

                try:
                    value = float(marks)
                except ValueError:
                    raise ValueError(f"Wrong data at line {number}: {marks}")

                if value < 0 or value > 100:
                    raise ValueError(f"Marks are not valid at line {number}: {marks}")

                print("Marks:", value)

    except FileNotFoundError:
        print("Unable to find file:", file_name)

    except ValueError as error:
        print("Error:", error)

    finally:
        print("File checking completed.")


if __name__ == "__main__":

    student_list = [
        Student("Raghu", 88),
        Student("Raghavendra", 74),
        Student("Naveen", 39)
    ]

    try:
        student_list[0].update_marks(150)
    except ValueError as error:
        print("Marks validation:", error)

    print("\nStudent Information:")

    for student in student_list:
        print(student)

    save_student_data(student_list)

    print("\nText File Content:")
    with open("students.txt", "r", encoding="utf-8") as file:
        print(file.read())

    print("CSV File Content:")
    with open("students.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print(list(reader))

    print("JSON File Content:")
    with open("students.json", "r", encoding="utf-8") as file:
        print(json.load(file))

    with open("marks_valid.txt", "w", encoding="utf-8") as file:
        file.write("85\n70\n")

    with open("marks_invalid.txt", "w", encoding="utf-8") as file:
        file.write("85\nwrong-data\n")

    print("\nChecking Valid File:")
    check_marks_file("marks_valid.txt")

    print("\nChecking Missing File:")
    check_marks_file("missing_marks.txt")

    print("\nChecking Invalid File:")
    check_marks_file("marks_invalid.txt")
