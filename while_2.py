# input 5 student --> list
# print them
students = []
i = 1 # int
while len(students) < 5:
    std = input("please input student number " + str(i) + "\n")
    i = i + 1
    students.append(std)

print(students)
