
def menu():
    print("Please choose the following")
    print("1 : Rectangle")
    print("2 : Square")
    print("3 : Circle")
    print("Any number to quit")


def square():
    print("Please enter the side of the square")
    side = int(input())
    perimeter = side * 4
    area = side * side
    print("perimeter is: " + str(perimeter))
    print("Area is: " + str(area))


def rectangle():
    print("Please enter the length of the rectangle")
    length = int(input())
    print("Please enter the width of the rectangle")
    width = int(input())
    perimeter = (width + length) * 2
    area = length * width
    print("perimeter is: " + str(perimeter))
    print("Area is: " + str(area))

def circle():
    print("Please enter the radius of the circle")
    radius = int(input())
    circumfrence = radius * 2 * 3.14
    area = (radius * radius) * 3.14
    print("circumfrence is: " + str(circumfrence))
    print("Area is: " + str(area))




print("Welcome Rayan")
menu()
option = int(input())
if option == 1:
    rectangle()
elif option == 2:
    square()
elif option == 3:
    circle()
else:
    print("You are dumb, Goodbye")