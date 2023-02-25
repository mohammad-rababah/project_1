from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = self.radius ** 2 * pi
        return area

    def circ(self):
        circ = self.radius * 2 * pi
        return circ


c1 = Circle(5)
c2 = Circle(10)
if c1.area() < c2.area():
    print(True)
