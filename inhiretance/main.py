from inhiretance.ball import Ball
from inhiretance.cylinder import Cylinder

b_1 = Ball(1)
b_1.print_area()

cy = Cylinder(4, 20)
print("the area is :" + str(cy.area()))
print("the mo7ee6 is :" + str(cy.circ()))
print("the area of the base :" + str(cy.get_base().area()))
