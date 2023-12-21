testScores = {
    "Harry": 81,
    "Ron": 78,
    "Hermoine": 99,
    "Draco": 74,
    "Neville": 62,
}

studentGrades = {}

for student, grades in testScores.items():
    if grades < 70:
        studentGrades[student] = "Fail"
    elif grades < 80:
        studentGrades[student] = "Acceptable"
    elif grades < 90:
        studentGrades[student] = "Exceeds Expectations"
    else:
        studentGrades[student] = "Outstanding"

print(studentGrades)
