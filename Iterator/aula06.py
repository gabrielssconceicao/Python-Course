from itertools import groupby
students = [
    {"name": "Alice Johnson", "subject": "Math", "grade": "B"},
    {"name": "Bob Smith", "subject": "History", "grade": "A"},
    {"name": "Charlie Brown", "subject": "Science", "grade": "C"},
    {"name": "Daisy Miller", "subject": "English", "grade": "A"},
    {"name": "Ethan Davis", "subject": "Art", "grade": "B"},
    {"name": "Fiona Wilson", "subject": "Math", "grade": "A"},
    {"name": "George Clark", "subject": "History", "grade": "B"},
    {"name": "Hannah Lewis", "subject": "Science", "grade": "B"},
    {"name": "Ian Walker", "subject": "English", "grade": "C"},
    {"name": "Jasmine Harris", "subject": "Art", "grade": "A"}
]


def order(student):
    return student['grade']


grouped_students = sorted(students, key=order)
groups = groupby(grouped_students,  key=order)

for key, group in groups:
    print("Grade:",key)
    for student in group:
        print("\t", student)
        
