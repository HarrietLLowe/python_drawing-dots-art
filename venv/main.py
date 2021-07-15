import turtle as t
import random

colors = [(201, 164, 112), (152, 75, 50), (221, 201, 138), (57, 95, 126), (170, 152, 44), (138, 31, 20), (135, 163, 183), (196, 94, 75), (49, 121, 88), (143, 177, 149), (95, 75, 77), (76, 39, 32), (164, 146, 157), (16, 98, 71), (232, 176, 165), (54, 46, 48), (32, 61, 76), (22, 83, 89), (182, 204, 176), (141, 22, 25), (86, 147, 127), (45, 66, 85), (8, 68, 53), (177, 94, 97), (222, 177, 182), (109, 128, 151)]

t_turtle = t.Turtle()
t_turtle.hideturtle()
t.colormode(255)
t_turtle.pensize(20)
dots = 0
y_coord = -250

def random_color():
    r = random.choice(colors[0])
    g = random.choice(colors[1])
    b = random.choice(colors[2])
    color_rgb = (r, g, b)
    return color_rgb


def print_dots():
    for x in range(0, 10):
        global dots
        dots += 1
        t_turtle.color(random_color())
        t_turtle.pendown()
        t_turtle.forward(1)
        t_turtle.penup()
        t_turtle.forward(50)


def set_position():
    t_turtle.penup()
    t_turtle.setpos(-350,-250)


def change_position(x, y):
    t_turtle.setpos(x, y)


def new_position():
    for n in range(10):
        global y_coord
        y_coord += 5
        change_position(-350, y_coord)

def main():
    set_position()
    tp = t_turtle.pos()
    while dots < 100:
        print_dots()
        new_position()

main()

screen = t.Screen()
screen.exitonclick()