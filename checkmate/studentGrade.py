print("NAME OF SCHOOL: LAGBAJA SCHOOL")
teacher_name = input("Name of teacher: ")
num_students = int(input("Enter number of students: "))
num_subjects = int(input("Enter number of subjects: "))

student_grades = []
student_totals = []
student_averages = []

for student in range(1, num_students + 1):
        grades = []
        total = 0
        for subject in range(1, num_subjects + 1):
            grade = int(input(f"Student {student}, Subject {subject}: "))
            grades.append(grade)
            total += grade
        average = total / num_subjects
        student_grades.append(grades)
        student_totals.append(total)
        student_averages.append(average)
print("\nSTUDENT\t", end="")
for i in range(1, num_subjects + 1):
        print(f"\tSUB{i}", end="")
print("\tTOT\tAVE\tPOS\n")

for i, grades in enumerate(student_grades):
    print(f"Student {i+1}\t", end="")
for grade in grades:
    print(f"{grade}\t", end="")
    print(f"{student_totals[i]}\t{student_averages[i]:.2f}\t")

