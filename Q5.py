school = {}
while True:
    print("please input your choice")
    print("1- add class ")
    print("2- add student to class ")
    print("3- print school")
    print("4- print single student from class")
    print("5- exit")
    choice = input()  # string
    if choice == "1":
        cls = input("please input your class\n")
        school[cls] = []
    elif choice == "2":
        cls = input("please input your class\n")
        std = input("please input your student\n")
        school[cls].append(std)
    elif choice == "3":
        print(school)
    elif choice == "4":
        cls = input("please input your class\n")
        students = school[cls]
        if len(students) == 0:
            print("you dont have any students")
            continue
        print("your index range from 0 to " + str(len(students) - 1))
        index = int(input("please input student index\n"))  # sting
        print(students[index])
    elif choice == "5":
        break
    else:
        print("invalid input")
        continue
    print("thanks")

print("program end")
