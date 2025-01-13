n = int(input())

students_list = []
for _ in range(n):
    student = input().split()
    student[1] = int(student[1])
    student = tuple(student)
    students_list.append(student)
    
students_list = sorted(students_list, key=lambda x: x[1])

for s in students_list:
    print(s[0], end=' ')