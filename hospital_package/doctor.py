from hospital_package.person import Person


class Doctor(Person):
    def inputs_dat(self):
        super(Doctor, self).inputs_dat()
        self.hour_rate = float(input("please input doc hour_rate"))
        self.major = input("please input doc major")
        return self

    def print_info(self):
        super(Doctor, self).print_info()
        print("major = " + self.major)
        print("hour_rate = " + str(self.hour_rate))
