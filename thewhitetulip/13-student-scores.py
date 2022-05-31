csv_file = open("students.csv", "r")
students = csv_file.readlines()
students = [student.strip() for student in students]

heading = students[0].split(',')
students = students[1:]
total_subjects = len(heading)
marks = {}

for i in range(len(students)):
    score = students[i].split(",")
    marks[score[0]] = sum([int(j) for j in score[1:]])

for name in marks.keys():
    print("%s: %d" % (name, marks[name]))
