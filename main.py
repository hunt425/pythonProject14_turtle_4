###########################################################
#Hunter Tysdal
#CompSci_Lab2
#12/2/2021

import turtle


class Point(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()

    def draw_action(self):
        turtle.dot()


class Box(Point):
    def __init__(self, x1, y1, width, height, color):
        self.x1 = x1
        self.y1 = y1
        self.width = width
        self.height = height
        self.color = color
        super().__init__(x1, y1, color)

    def draw_action(self):
        turtle.penup()
        turtle.goto(self.x1, self.y1)
        turtle.pendown()
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.pendown()


class Boxfilled(Box):
    def __init__(self, x1, y1, width, height, color, fillcolor):
        super().__init__(x1, y1, width, height, color)
        self.fillcolor = fillcolor

    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Box.draw_action(self)
        turtle.end_fill()


class Circle(Point):
    def __init__(self, x1, y1, radius, color):
        super().__init__(x1, y1, color)
        self.radius = radius

    def draw_action(self):
        turtle.circle(self.radius)


class CircleFilled(Circle):
    def __init__(self, x1, y1, radius, color, fillcolor):
        super().__init__(x1, y1, radius, color)
        self.fillcolor = fillcolor

    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Circle.draw_action(self)
        turtle.end_fill()


p = Point(-100, 100, 'blue')
b = Box(100, 110, 50, 40, 'red')
c = Boxfilled(100, 110, 50, 40, 'red', 'blue')
t = Circle(50, 75, 40, 'green')
m = CircleFilled(50, 75, 40, 'green', 'brown')

# p.draw()
# b.draw()
c.draw()
# t.draw()
m.draw()
