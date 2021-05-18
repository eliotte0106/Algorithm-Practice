n = int(input())
grade = []
for i in range(n):
    data = input().split()
    grade.append((data[0],int(data[1])))

grade = sorted(grade, key = lambda student: student[1]) #sort by score

for student in grade: # print only name with space
    print(student[0], end = " ")

