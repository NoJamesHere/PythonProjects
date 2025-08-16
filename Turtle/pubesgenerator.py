import turtle
import random

running = True

def settingfalse():
    global running
    running = False

def turn_random():
    angle = random.randint(-90, 90)
    turtle.left(angle)

screen = turtle.Screen()
screen.setup(width=600, height=600)   # window size
screen.bgcolor("purple")

turtle.shape("square")
turtle.shapesize(1)
turtle.speed(0)

turtle.onkeypress(settingfalse, "Return")
turtle.listen()

# get window boundaries (half-width/height)
half_width = screen.window_width() // 2
half_height = screen.window_height() // 2

while running:
    turtle.forward(20)
    x, y = turtle.xcor(), turtle.ycor()

    # check if turtle hits boundary
    if abs(x) > half_width or abs(y) > half_height:
        turtle.setheading(turtle.towards(0, 0))

    turn_random()

turtle.bye()