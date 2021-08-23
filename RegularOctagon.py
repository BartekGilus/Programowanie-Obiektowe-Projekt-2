from ConvexPolygon import ConvexPolygon
import Descryptors as desc
import math

class RegularOctagon(ConvexPolygon):

    fill_colour = desc.ColorV()
    outline_colour = desc.ColorV()

    length_of_a = desc.SideV()

    def __init__(self, fill_colour, outline_colour):
        super().__init__(fill_colour, outline_colour)
        self.set_parameters()

    def set_parameters(self):
        self.length_of_a = input("Podaj długość boku: ")

    def scale(self):
        if self.length_of_a <= 5:
            return 22
        else:
            return 10

    def vector(self):
        if self.length_of_a <= 10:
            return 8
        else:
            return 5

    def area(self):
        a = self.length_of_a
        return 2 * (1 + math.sqrt(2)) * math.pow(a, 2)

    def perimeter(self):
        return 8 * self.length_of_a

    def draw(self):
        a = self.length_of_a
        start_x = self.vector()
        start_y = self.vector()
        coords = []
        angle = 45
        for i in range(8):
            end_x = start_x + a * math.cos(math.radians(angle * i))
            end_y = start_y + a * math.sin(math.radians(angle * i))
            coords.append([self.scale() * start_x, self.scale() * start_y])
            start_x = end_x
            start_y = end_y
        return coords