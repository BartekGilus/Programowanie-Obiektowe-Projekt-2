from ConvexQuadrilateral import ConvexQuadrilateral
import math

class Parallelogram(ConvexQuadrilateral):

    def __init__(self, fill_colour, outline_colour):
        super().__init__(fill_colour, outline_colour)

    def set_parameters(self):
        self.length_of_a = input("Podaj długość boku: ")
        self.length_of_b = input("Podaj długość boku: ")
        self.length_of_c = self.length_of_a
        self.length_of_d = self.length_of_b
        self.angle_one = input("Podaj szerokość kąta: ")
        self.angle_two = 180 - self.angle_one
        self.angle_three = self.angle_one
        self.angle_four = self.angle_two

class Rhombus(Parallelogram):

    def __init__(self, fill_colour, outline_colour):
        super().__init__(fill_colour, outline_colour)

    def set_parameters(self):
        self.length_of_a = input("Podaj długość boku: ")
        self.length_of_b = self.length_of_a
        self.length_of_c = self.length_of_a
        self.length_of_d = self.length_of_a
        self.angle_one = input("Podaj szerokość kąta: ")
        self.angle_two = 180 - self.angle_one
        self.angle_three = self.angle_one
        self.angle_four = self.angle_two

class Square(Parallelogram):

    def __init__(self, fill_colour, outline_colour):
        super().__init__(fill_colour, outline_colour)

    def set_parameters(self):
        self.length_of_a = input("Podaj długość boku: ")
        self.length_of_b = self.length_of_a
        self.length_of_c = self.length_of_a
        self.length_of_d = self.length_of_a
        self.angle_one = 90
        self.angle_two = 90
        self.angle_three = 90
        self.angle_four = 90

class Kite(ConvexQuadrilateral):

    def __init__(self, fill_colour, outline_colour):
        super().__init__(fill_colour, outline_colour)

    def set_parameters(self):
        self.length_of_a = input("Podaj długość boku: ")
        self.length_of_b = input("Podaj długość boku: ")
        self.length_of_c = self.length_of_b
        self.length_of_d = self.length_of_a
        self.angle_one = input("Podaj szerokość kąta: ")
        self.angle_two = input("Podaj szerokość kąta: ")
        self.angle_three = self.angle_two
        self.angle_four = 360 - self.angle_one - 2 * self.angle_two

    def area(self):
        a = self.length_of_a
        b = self.length_of_b
        return ((math.pow(a, 2) * math.sin(math.radians(self.angle_one))) / 2) + ((math.pow(b, 2) * math.sin(math.radians(360 - (self.angle_one + 2 * self.angle_two)))) / 2)

    def draw(self):
        side_a = self.length_of_a
        side_b = self.length_of_b
        ang1 = self.angle_one
        p1 = 2 * side_a * math.cos(math.radians((180 - ang1) / 2))
        p2 = side_a * math.cos(math.radians(ang1 / 2)) + side_b * math.cos(math.radians((180 - ang1) / 2))

        h = math.sqrt(math.pow(side_a, 2) - (math.pow(p1, 2)) / 4)

        A = (self.vector(), self.vector())
        B = (p2 + self.vector(), self.vector())

        S = (p2 + self.vector() - h, self.vector())

        C = (S[0], self.vector() - p1 / 2)
        D = (S[0], self.vector() + p1 / 2)

        coords = [int((x + 1) * self.scale()) for x in A + C + B + D]
        return coords