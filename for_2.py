tup = (10, 30, -15, 2.4, "mohammad", False)
# search ---> 2.4
# if value in the for loop == 2.4 found = true
# found == false
# output -> found or not found

found = False
for t in tup:
    if t == 2.4:
        found = True
        break
    if t == -15:
        continue
    print(t)

if found == True:
    print("founded")
else:
    print("not founded")
