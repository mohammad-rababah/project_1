class Person():

    def inputs_dat(self):
        self.name = input("please input doc name")
        self.age = input("please input doc age")
        return self

    def print_info(self):
        print("name = " + self.name)
        print("age = " + self.age)
