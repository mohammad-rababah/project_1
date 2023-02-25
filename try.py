def rase_exception():
    age = int(input("please input your age"))
    if age > 120:
        raise Exception("input correct age")


try:
    rase_exception()
except  Exception as exp:
    print(exp)
