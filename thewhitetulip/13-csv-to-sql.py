file_name = "students.csv"
input_file = open(file_name, "r")
output_file = open("students.sql", "w")

csv_lines = input_file.readlines()
csv_lines = [line.strip() for line in csv_lines]

INSRT_STMT = 'INSERT INTO STUDENT(NAME, SCIENCE, MATH, HISTORY) VALUES('

inserts = []

for line in csv_lines[1:]:
    iline = line.split(",")
    insert = INSRT_STMT + '"' + iline[0] + '"'
    for i in iline[1:]:
        insert += ","
        insert += i
    insert += ");\n"
    inserts.append(insert)

output_file.writelines(inserts)
output_file.close()
