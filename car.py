# name
# cylinder
# color
# model
# price

class Car:
    name = ""
    cylinder = 0
    color = ""
    model = 1900
    price = 0.0

    def __init__(self, name, cylinder, color, model, price):
        print("new car")
        self.name = name
        self.cylinder = cylinder
        self.color = color
        self.model = model
        self.price = price


car_1 = Car("accent", 4, "Red", 2005, 5000)
car_2 = Car("prious", 6, "Blue", 2015, 15000)

print(car_1.name)
