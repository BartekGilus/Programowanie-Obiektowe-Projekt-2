from  ConvexPolygon import ConvexPolygon
import Descryptors as desc
import math

class ConvexQuadrilateral(ConvexPolygon):
    fill_colour = desc.ColorV()
    outline_colour = desc.ColorV()

    length_of_a = desc.SideV()
    length_of_b = desc.SideV()
    length_of_c = desc.SideV()
    length_of_d = desc.SideV()

    angle_one = desc.AngleV()
    angle_two = desc.AngleV()
    angle_three = desc.AngleV()
    angle_four = desc.AngleV()

    def __init__(self, fill_colour, outline_colour):
        super().__init__(fill_colour, outline_colour)
        self.set_parameters()

    def set_parameters(self):
        self.length_of_a = input("Podaj długość boku: ")
        self.length_of_b = input("Podaj długość boku: ")
        self.length_of_c = input("Podaj długość boku: ")
        self.length_of_d = input("Podaj długość boku: ")
        self.angle_one = input("Podaj szerokość kąta: ")
        self.angle_two = input("Podaj szerokość kąta: ")
        self.angle_three = input("Podaj szerokość kąta: ")
        self.angle_four = 360 - (self.angle_one + self.angle_two + self.angle_three)

    def scale(self):
        if self.length_of_a <= 5 and self.length_of_b <= 5 and self.length_of_c <= 5 and self.length_of_d <= 5:
            return 22
        else:
            return 10

    def vector(self):
        if self.length_of_a <= 10 and self.length_of_b <= 10 and self.length_of_c <= 10 and self.length_of_d <= 10:
            return 8
        else:
            return 10

    def area(self):
        h = self.length_of_b * math.sin(math.radians(self.angle_one))
        return self.length_of_a * h

    def perimeter(self):
        return self.length_of_a + self.length_of_b + self.length_of_c + self.length_of_d

    def draw(self):
        side_one = self.length_of_a
        side_three = self.length_of_c
        side_four = self.length_of_d
        a = side_one * math.cos(math.radians(self.angle_one))
        c = side_three * math.cos(math.radians(self.angle_three))
        d = side_four * math.sin(math.radians(self.angle_four))

        coords = [
            (self.scale() * self.vector(), self.scale() * self.vector()),
            (self.scale() * (self.vector() + side_one), self.scale() * self.vector()),
            (self.scale() * (self.vector() + side_three + a), self.scale() * (self.vector() + d)),
            (self.scale() * (self.vector() + c), self.scale() * (self.vector() + d))
        ]

        return coords