import turtle
import colorsys


def draw_circle(turtle_obj, radius, color):
    turtle_obj.color(color)
    turtle_obj.penup()
    turtle_obj.goto(0, -radius)
    turtle_obj.pendown()
    turtle_obj.circle(radius)


def draw_rangoli():
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Colorful Rangoli")

    rangoli_turtle = turtle.Turtle()
    rangoli_turtle.speed(0)

    num_circles = 36
    radius = 150
    hue = 0

    for _ in range(num_circles):
        color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        draw_circle(rangoli_turtle, radius, color)
        rangoli_turtle.right(360 / num_circles)
        hue += 1 / num_circles

    screen.mainloop()


draw_rangoli()
