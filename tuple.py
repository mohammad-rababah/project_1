A = (10, 20, 30, 40, 30, 20)  # tuple
# ordered unchangeable allow duplicate
B = [10, 20, 30, 40]  # list
#  ordered changeable allow duplicate
C = {10, 20, 30}  # set
# not ordered changeable not allowed duplicate
print(len(C))
C.add(250)
C.add(250)
print(print(C))
print(A[1:3])
print(len(A))
print(B)
B.append(20)
print(B)
