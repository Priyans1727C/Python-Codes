def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

students = [
    {"name": "Alice", "grades": [85, 90, 92]},
    {"name": "Bob", "grades": [78, 80, 85]},
    {"name": "Charlie", "grades": [95, 88, 92]},
    {"name": "David", "grades": [87, 82, 80]}
]

print("Student Information:")
for student in students:
    print(f"{student['name']}: Grades {student['grades']}")

all_grades = [grade for student in students for grade in student["grades"]]
average_grade = calculate_average(all_grades)
print(f"\nClass Average Grade: {average_grade:.2f}")

highest_grade_student = max(students, key=lambda x: max(x["grades"]))
print(f"\nStudent with the Highest Grade: {highest_grade_student['name']}")

lowest_grade_student = min(students, key=lambda x: min(x["grades"]))
print(f"Student with the Lowest Grade: {lowest_grade_student['name']}")
