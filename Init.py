from Triangles import Triangle, IsoscelesTriangle, EquilateralTriangle
from RegularPentagon import RegularPentagon
from RegularHexagon import RegularHexagon
from RegularOctagon import RegularOctagon
from ConvexQuadrilateral import ConvexQuadrilateral
from Quadrilaterals import Parallelogram, Kite, Rhombus, Square

class Init():

    def triangle(self, canvas):
        fill_c = input("Podaj kolor wypełniena [black, red, blue, yellow, green]: ")
        outline_c = input("Podaj kolor obwódki [black, red, blue, yellow, green]: ")
        p = Triangle(fill_c, outline_c)
        canvas.create_polygon(p.draw(), fill=p.fill_colour, outline=p.outline_colour)
        canvas.create_text(300, 580, fill="black", text="Pole: " + str(p.area()) + "\t Obwód: " + str(p.perimeter()))

    def isoscelesTriangle(self, canvas):
        fill_c = input("Podaj kolor wypełniena [black, red, blue, yellow, green]: ")
        outline_c = input("Podaj kolor obwódki [black, red, blue, yellow, green]: ")
        p = IsoscelesTriangle(fill_c, outline_c)
        canvas.create_polygon(p.draw(), fill=p.fill_colour, outline=p.outline_colour)
        canvas.create_text(300, 580, fill="black", text="Pole: " + str(p.area()) + "\t Obwód: " + str(p.perimeter()))

    def equilateralTriangle(self, canvas):
        fill_c = input("Podaj kolor wypełniena [black, red, blue, yellow, green]: ")
        outline_c = input("Podaj kolor obwódki [black, red, blue, yellow, green]: ")
        p = EquilateralTriangle(fill_c, outline_c)
        canvas.create_polygon(p.draw(), fill=p.fill_colour, outline=p.outline_colour)
        canvas.create_text(300, 580, fill="black", text="Pole: " + str(p.area()) + "\t Obwód: " + str(p.perimeter()))

    def regularPentagon(self, canvas):
        fill_c = input("Podaj kolor wypełniena [black, red, blue, yellow, green]: ")
        outline_c = input("Podaj kolor obwódki [black, red, blue, yellow, green]: ")
        p = RegularPentagon(fill_c, outline_c)
        canvas.create_polygon(p.draw(), fill=p.fill_colour, outline=p.outline_colour)
        canvas.create_text(300, 580, fill="black", text="Pole: " + str(p.area()) + "\t Obwód: " + str(p.perimeter()))

    def regularHexagon(self, canvas):
        fill_c = input("Podaj kolor wypełniena [black, red, blue, yellow, green]: ")
        outline_c = input("Podaj kolor obwódki [black, red, blue, yellow, green]: ")
        p = RegularHexagon(fill_c, outline_c)
        canvas.create_polygon(p.draw(), fill=p.fill_colour, outline=p.outline_colour)
        canvas.create_text(300, 580, fill="black", text="Pole: " + str(p.area()) + "\t Obwód: " + str(p.perimeter()))

    def regularOctagon(self, canvas):
        fill_c = input("Podaj kolor wypełniena [black, red, blue, yellow, green]: ")
        outline_c = input("Podaj kolor obwódki [black, red, blue, yellow, green]: ")
        p = RegularOctagon(fill_c, outline_c)
        canvas.create_polygon(p.draw(), fill=p.fill_colour, outline=p.outline_colour)
        canvas.create_text(300, 580, fill="black", text="Pole: " + str(p.area()) + "\t Obwód: " + str(p.perimeter()))

    def convexQuadrilateral(self, canvas):
        fill_c = input("Podaj kolor wypełniena [black, red, blue, yellow, green]: ")
        outline_c = input("Podaj kolor obwódki [black, red, blue, yellow, green]: ")
        p = ConvexQuadrilateral(fill_c, outline_c)
        canvas.create_polygon(p.draw(), fill=p.fill_colour, outline=p.outline_colour)
        canvas.create_text(300, 580, fill="black", text="Pole: " + str(p.area()) + "\t Obwód: " + str(p.perimeter()))

    def parallelogram(self, canvas):
        fill_c = input("Podaj kolor wypełniena [black, red, blue, yellow, green]: ")
        outline_c = input("Podaj kolor obwódki [black, red, blue, yellow, green]: ")
        p = Parallelogram(fill_c, outline_c)
        canvas.create_polygon(p.draw(), fill=p.fill_colour, outline=p.outline_colour)
        canvas.create_text(300, 580, fill="black", text="Pole: " + str(p.area()) + "\t Obwód: " + str(p.perimeter()))

    def kite(self, canvas):
        fill_c = input("Podaj kolor wypełniena [black, red, blue, yellow, green]: ")
        outline_c = input("Podaj kolor obwódki [black, red, blue, yellow, green]: ")
        p = Kite(fill_c, outline_c)
        canvas.create_polygon(p.draw(), fill=p.fill_colour, outline=p.outline_colour)
        canvas.create_text(300, 580, fill="black", text="Pole: " + str(p.area()) + "\t Obwód: " + str(p.perimeter()))

    def rhombus(self, canvas):
        fill_c = input("Podaj kolor wypełniena [black, red, blue, yellow, green]: ")
        outline_c = input("Podaj kolor obwódki [black, red, blue, yellow, green]: ")
        p = Rhombus(fill_c, outline_c)
        canvas.create_polygon(p.draw(), fill=p.fill_colour, outline=p.outline_colour)
        canvas.create_text(300, 580, fill="black", text="Pole: " + str(p.area()) + "\t Obwód: " + str(p.perimeter()))

    def square(self, canvas):
        fill_c = input("Podaj kolor wypełniena [black, red, blue, yellow, green]: ")
        outline_c = input("Podaj kolor obwódki [black, red, blue, yellow, green]: ")
        p = Square(fill_c, outline_c)
        canvas.create_polygon(p.draw(), fill=p.fill_colour, outline=p.outline_colour)
        canvas.create_text(300, 580, fill="black", text="Pole: " + str(p.area()) + "\t Obwód: " + str(p.perimeter()))