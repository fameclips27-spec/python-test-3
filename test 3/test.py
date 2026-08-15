students = {
    "david" : 20,
    "mark" : 75,
    "maro" : 40,
    "John" : 60,
    "Joshua" : 90,
}
total = 0
for score in students.values():
    total = total + score

average = total / len(students)

print("Class Average: ",average)

highest_score = max(students, key=students.get)
lowest_score = min(students, key=students.get)

print("Top Student: ",highest_score,students[highest_score])
print("lowest Student: ",lowest_score,students[lowest_score])

name_student = input("Enter a students name for score search: ")

score = students.get(name_student)

if score:
    print(name_student, "Scored", score)
else:
    print("Student not seen")