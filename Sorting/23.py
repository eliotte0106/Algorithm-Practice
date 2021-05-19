'''
korean, english, math
sort by korean score(decreasing)
if korean score is same, sort by english(increasing)
if english score is same, sort by math score(decreasing)
if all same, sort by name in dictionary form
'''

n = int(input())
grade = []

for i in range(n):
    grade.append(input().split())

#the elements are stored as tuple in the list, so we can do this below.
grade.sort(key = lambda x : (-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for student in grade:
    print(student[0])
