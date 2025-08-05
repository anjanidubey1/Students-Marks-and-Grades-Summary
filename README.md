# Student Marks Analyzer and Grade Summary System

## Project Description

This Python project is designed to take input of marks obtained by multiple students in three subjects and generate a summary report showing each student’s total marks, average, and grade. The program also calculates the class average and identifies the topper among all students.

This project is ideal for beginners who want to understand how to apply basic programming concepts like loops, conditionals, list manipulation, dictionaries, and formatted output in Python.

## Features

- Accepts student names and marks for 3 subjects
- Calculates:
  - Total and average marks per student
  - Grade based on average marks
  - Class average
  - Topper of the class
- Clean, console-based interface for input and output
- Modular and beginner-friendly code

## Input

- Number of students (integer)
- Student name (string)
- Marks for 3 subjects per student (integers)

### Example Input:
Enter number of students: 2

Enter details for student 1:
Name: Anjali
Enter marks for Subject 1: 78
Enter marks for Subject 2: 85
Enter marks for Subject 3: 90

Enter details for student 2:
Name: Rohan
Enter marks for Subject 1: 92
Enter marks for Subject 2: 88
Enter marks for Subject 3: 95

## Output

Displays:
- Name, marks, total, average, and grade for each student
- Class average
- Name of the topper

### Sample Output:
Student Summary:
Name: Anjali
Marks: [78, 85, 90]
Total: 253
Average: 84.33
Grade: A
Name: Rohan
Marks: [92, 88, 95]
Total: 275
Average: 91.67
Grade: A+
Class Average: 88.00
Topper: Rohan

## Grade Criteria

| Average Marks | Grade |
|---------------|-------|
| 90 - 100      | A+    |
| 80 - 89       | A     |
| 70 - 79       | B     |
| 60 - 69       | C     |
| 50 - 59       | D     |
| Below 50      | F     |

## Technologies Used

- *Language*: Python 3
- *Libraries*: None (uses only standard input/output and basic Python features)
