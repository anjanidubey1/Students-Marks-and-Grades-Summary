# Student Marks and Grades Summary

def calculate_grade(avg):
    if avg >= 90:
        return 'A+'
    elif avg >= 80:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 60:
        return 'C'
    elif avg >= 50:
        return 'D'
    else:
        return 'F'

# Input number of students
num_students = int(input("Enter number of students: "))

students = []
class_total = 0
topper = None
highest_total = 0

# Input and processing
for i in range(num_students):
    print(f"\nEnter details for student {i+1}:")
    name = input("Name: ")
    marks = []
    for j in range(3):
        mark = int(input(f"Enter marks for Subject {j+1}: "))
        marks.append(mark)
    
    total = sum(marks)
    average = total / 3
    grade = calculate_grade(average)
    
    student = {
        'name': name,
        'marks': marks,
        'total': total,
        'average': average,
        'grade': grade
    }
    
    students.append(student)
    class_total += average

    if total > highest_total:
        highest_total = total
        topper = name

# Output
print("\nStudent Summary:")
print("="*50)
for student in students:
    print(f"Name: {student['name']}")
    print(f"Marks: {student['marks']}")
    print(f"Total: {student['total']}")
    print(f"Average: {student['average']:.2f}")
    print(f"Grade: {student['grade']}")
    print("-"*50)

class_average = class_total / num_students
print(f"\nClass Average: {class_average:.2f}")
print(f"Topper: {topper}")