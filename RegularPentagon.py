from ConvexPolygon import ConvexPolygon
import Descryptors as desc
import math

class RegularPentagon(ConvexPolygon):

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
            return 25
        else:
            return 10

    def vector(self):
        if self.length_of_a <= 10:
            return 8
        else:
            return 5

    def area(self):
        a = self.length_of_a
        return (math.pow(a, 2) / 4) * math.sqrt(25 + (10 * math.sqrt(5)))

    def perimeter(self):
        return 5 * self.length_of_a

    def draw(self):
        a = self.length_of_a
        start_x = self.vector()
        start_y = self.vector()
        coords = []
        angle = 72
        for i in range(5):
            end_x = start_x + a * math.cos(math.radians(angle * i))
            end_y = start_y + a * math.sin(math.radians(angle * i))
            coords.append([self.scale() * start_x, self.scale() * start_y])
            start_x = end_x
            start_y = end_y
        return coords