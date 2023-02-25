# print 1 -> add student, 2-> print all  students ,3->exit
# input -> 3 cases
# if input = 1
students = []
while True:
    print("please input your choice")
    print("1- add student ")
    print("2- print students")
    print("3- print single student")
    print("4- exit")
    choice = input()  # string
    if choice == "1":
        std = input("please input new student name\n")
        students.append(std)
    elif choice == "2":
        print(students)
    elif choice == "3":
        if len(students) == 0:
            print("you dont have any students")
            continue
        print("your index range from 0 to " + str(len(students)-1))
        index = int(input("please input student index\n"))  # sting
        print(students[index])
    elif choice == "4":
        break
    else:
        print("invalid input")
        continue
    print("thanks")

print("program end")
