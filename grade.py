# calculate  avg from 3 marks output
# A -> 90
# B -> 80 - 90
# C -> 70 - 80
# D -> 60 - 70
# F -> > 60


# inputs -> (done)
# mark_1 , mark_2 , mark_3
# marks are valid
# 1 - calculate avg ---> (mark_1+mark_2+mark_3) / 3.0
# output -> print(A or B or ....)
mark_1 = int(input("please input first mark\n"))
mark_2 = int(input("please input second mark\n"))
mark_3 = int(input("please input third mark\n"))

if mark_1 < 0 or mark_1 > 100:
    print("mark 1 is invalid")
elif mark_2 < 0 or mark_2 > 100:
    print("mark 2 is invalid")
elif mark_3 < 0 or mark_3 > 100:
    print("mark 3 is invalid")
else:
    avg = (mark_1 + mark_2 + mark_3) / 3
    print("your avg is " + str(avg))
    if avg >= 90:
        print("A")
    elif avg >= 80:
        print("B")
    elif avg >= 70:
        print("C")
    elif avg >= 60:
        print("D")
    else:
        print("F")
