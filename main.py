from turtle import Turtle, Screen, colormode
import colorgram
import random
colormode(255)
timmy = Turtle()
colours = ["CornflowerBlue", "DeepSkyBlue", "LightSeaGreen", "SlateGray", "SeaGreen"]
timmy.speed(20)
# def move():
#     direction = 90 * random.randint(0, 3)
#     timmy.color(random.choice(colours))
#     timmy.left(direction)
#     timmy.forward(20)
#
# for _ in range(50):
#     move()

# def spiral(radius, angle):
#
#     count = int(round(360 / angle))
#     timmy.color(random.choice(colours))
#     for _ in range(count):
#
#         timmy.circle(radius)
#         timmy.left(angle)
#
#
# shapes = random.randint(1, 10)
# for _ in range(shapes):
#     radius = random.randint(10, 100)
#     angle = random.randint(1, 90)
#     spiral(radius, angle)

# colors_rgb = []
# colors = colorgram.extract('image.jpg', 6)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r, g, b)
#     colors_rgb.append(color_tuple)
#
# print(colors_rgb)
right = True

colors_rgb = [(189, 221, 244), (127, 176, 214), (193, 227, 215), (182, 169, 126), (23, 38, 20), (154, 208, 217)]

def paint(color, radius):
    # set the fillcolor
    color_random = random.choice(color)
    timmy.fillcolor(color_random)
    timmy.pencolor(color_random)

    # start the filling color
    timmy.begin_fill()

    # drawing the circle of radius r
    timmy.circle(radius)

    # ending the filling of the color
    timmy.end_fill()

def movement(distance):
    timmy.penup()
    timmy.forward(distance)
    timmy.pendown()

def next_row(y_distance):
    rotate = 90
    timmy.left(rotate)
    movement(y_distance)
    timmy.left(rotate)
    movement(200)
    timmy.left(180)

def paint_circle(x, y, radius, color):
     y_distance = 200 / (y - 1)
     x_distance = 200 / (x - 1)
     for _ in range(y - 1):
        for __ in range(x - 1):
            paint(color, radius)
            movement(x_distance)

        next_row(y_distance)

paint_circle(5, 5, 10, colors_rgb)


screen = Screen()
screen.exitonclick()