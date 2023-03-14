i = 0
while i < 10:
    print(i)
    i += 1
    if i == 5:
        break
else:
    print(10)


def function_name(arg_1, arg_2):
    pass


class MyName():
    pass


X1 = {1, 2, 3}  # Set imutable order not grenteed
X2 = {1: 10, 20: 30}  # dict key-value mutable non order
X3 = [1, 2, 3]  # list mutable order
x4 = (1, 2, 3)  # tuble imutable order

number = 10 ** 2  # poweer
x = "ahmad" * 4
print(x)

x = "python"
print(x[-2])  #
print(x[1:-2])
y = [1, 20, 13, 4, 5]
y2 = [1, 3, 4, 5, 6]  # transpose

# (1,5) (5,1) -- > (1,1)

y3 = []
for i in range(len(y)):  # 0->4 as index
    y3.append(y[i] * y2[i])

print(y3)

x = ["a", "b"]
y = [1, 2]

# nestd for
for i in x:
    for j in y:
        print(i, j)

# 1 -- > a,1
# 2 ---> a,2
# 3 ---> b,1
# 4----> b,2
import numpy as np

x = np.array([5, 6, 6, 9, 8, 0, 3, 9, 7, 6, 1, 5, 8])
x = x[4:8]
print(x[1:])
print(x[:-1])
d = x[1:] - x[:-1]
print(d)
