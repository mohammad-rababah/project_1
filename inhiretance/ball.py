from math import pi

from inhiretance.circle import Circle


class Ball(Circle):

    def volume(self):
        v = (4 / 3) * pi * self.radius ** 3
        return v

    def area(self):
        return 4 * pi * self.radius ** 2

    def print_area(self):
        print("the area is " + str(super().area()))
