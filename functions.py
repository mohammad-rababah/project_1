# def print_welcome(name, age, array):
#     print("welcome " + name)
#     print("age is " + str(age))
#     for a in array:
#         print(a)
#
#
# print_welcome("sarah", 20, ["mohammad", "ali", "khlaed"])
# print_welcome("mohammad", 15, [])

# input 2 redis (done)
# calculate area or each (done)
# compare
# print whose bigger
def calculate_area(r):
    area = r ** 2 * 3.14
    return area


r1 = int(input("please input r1\n"))
r2 = int(input("please input r2\n"))
area1 = calculate_area(r1)
area2 = calculate_area(r2)

if area1 > area2:
    print("circle 1 is bigger")
elif area2 > area1:
    print("circle 2 is bigger")
else:
    print("circles are equal")

