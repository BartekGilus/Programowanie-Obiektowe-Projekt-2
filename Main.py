from tkinter import *
from Init import Init

if __name__ == '__main__':
    tk = Tk()
    init = Init()
    canvas = Canvas(width=800, height=600, bg="white")
    canvas.pack()
    print("Wybierz którą figure chcesz naryzować: \n"
              "1. Trójkąt \n"
              "2. Trójkąt równoramienny \n"
              "3. Trójkąt równoboczny \n"
              "4. Pięciokąt foremny \n"
              "5. Sześciokąt foremny \n"
              "6. Osimiokąt foremny \n"
              "7: Czworokąt \n"
              "8. Równoległobok \n"
              "9. Deltoid \n"
              "10.Romb \n"
              "11.Kwadrat \n"
              "0. Wyjście")

    argument = int(input("Wybierz opcje: "))

    if argument == 1:
        init.triangle(canvas)
    elif argument == 2:
        init.isoscelesTriangle(canvas)
    elif argument == 3:
        init.equilateralTriangle(canvas)
    elif argument == 4:
        init.regularPentagon(canvas)
    elif argument == 5:
        init.regularHexagon(canvas)
    elif argument == 6:
        init.regularOctagon(canvas)
    elif argument == 7:
        init.convexQuadrilateral(canvas)
    elif argument == 8:
        init.parallelogram(canvas)
    elif argument == 9:
        init.kite(canvas)
    elif argument == 10:
        init.rhombus(canvas)
    elif argument == 11:
        init.square(canvas)
    elif argument == 0:
        exit()
    else:
        print("Niewłaściwa opcja.")

    tk.mainloop()
