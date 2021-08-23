from ConvexPolygon import ConvexPolygon
import Descryptors as desc
import math

class Triangle(ConvexPolygon):

    fill_colour = desc.ColorV()
    outline_colour = desc.ColorV()

    length_of_a = desc.SideV()
    length_of_b = desc.SideV()
    length_of_c = desc.SideV()

    def __init__(self, fill_colour, outline_colour):
        super().__init__(fill_colour, outline_colour)
        self.set_parameters()

    def set_parameters(self):
        self.length_of_a = input("Podaj długość boku: ")
        self.length_of_b = input("Podaj długość boku: ")
        self.length_of_c = input("Podaj długość boku: ")

    def scale(self):
        if self.length_of_a <= 15 and self.length_of_b <= 15 and self.length_of_c <= 15:
            return 50
        else:
            return 20

    def area(self):
        a = self.length_of_a
        b = self.length_of_b
        c = self.length_of_c

        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    def perimeter(self):
        return self.length_of_a + self.length_of_b + self.length_of_c

    def draw(self):
        a = self.length_of_a
        b = self.length_of_b
        c = self.length_of_c

        A = (0, 0)
        B = (c, 0)
        hc = (2 * (a ** 2 * b ** 2 + b ** 2 * c ** 2 + c ** 2 * a ** 2) - (a ** 4 + b ** 4 + c ** 4)) ** 0.5 / (2. * c)
        dx = (b ** 2 - hc ** 2) ** 0.5
        if abs((c - dx) ** 2 + hc ** 2 - a ** 2) > 0.01: dx = -dx
        C = (dx, hc)

        coords = [int((x + 1) * self.scale()) for x in A + B + C]
        return coords

class IsoscelesTriangle(Triangle):

    def __init__(self, fill_colour, outline_colour):
        super().__init__(fill_colour, outline_colour)

    def set_parameters(self):
        self.length_of_a = input("Podaj długość boku: ")
        self.length_of_b = input("Podaj długość boku: ")
        self.length_of_c =  self.length_of_b

class EquilateralTriangle(Triangle):

    def __init__(self, fill_colour, outline_colour):
        super().__init__(fill_colour, outline_colour)

    def set_parameters(self):
        self.length_of_a = input("Podaj długość boku: ")
        self.length_of_b = self.length_of_a
        self.length_of_c =  self.length_of_a