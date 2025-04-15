student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for name in student_scores:
    score = student_scores[name]

    if 100 >= score >= 91:
        grade = "outstatding"
    elif 90 >= score >= 81:
        grade = "Exceeds Expectations"
    elif 80 >= score >= 71:
        grade = "Acceptable"
    else:
        grade = "fail"

    student_grades[name] = grade

print(student_grades)
