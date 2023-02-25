A = [1, 4, 9, 10]  # j -> 2
B = [2, 6, 7, 9]  # k -> 4
C = [] #->  1,2,4,6,7,9
j, k = 0, 0
length = len(A) + len(B)
for i in range(length):  # ---> 8
    if A[j] < B[k]:
        C.append(A[j])
        j = j + 1
    else:
        C.append(B[k])
        k = k + 1
    if k == len(B) or j == len(A):
        break

for i in range(j,len(A)):
    C.append(A[i])

for i in range(k,len(B)): # 4 --> 4
    C.append(B[k])

print(C)