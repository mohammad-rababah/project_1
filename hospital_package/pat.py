from hospital_package.person import Person


class Pat(Person):
    hour = 0

    def inputs_dat(self):
        super(Pat, self).inputs_dat()
        self.illness = input("please input doc age")
        return self

    def print_info(self):
        super(Pat, self).print_info()
        print("illness = " + self.illness)
        print("hour = " + str(self.hour))
