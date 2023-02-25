print("hello, please add your mark")
mark = input()
mark = int(mark)
# end of input
if mark > 100 or mark < 0:
    print("invalid")
    print("this is wrong")
elif mark >= 50:
    print("pass")
else:
    print("fail")

print("thank you")
# valid or not valid
# pass or fail
# mark >100 or mark < 0 -> invalid
# mark >= 50 -> pass
# mark < 50 (else) -> fail
