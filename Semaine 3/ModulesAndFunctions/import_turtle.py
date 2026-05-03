""" import turtle

turtle.pendown()
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.done() """

from math import cos, sin, radians

def trigo(angle, distance):
    angle = radians(angle)
    x = cos(angle) * distance
    y = sin(angle) * distance
    return x, y

angle = 90
distance = 100
x, y = trigo(angle, distance)
print(f"Angle: {angle}°")
print(f"Distance: {distance}")
print(f"X: {x}")
print(f"Y: {y}")

print(dir())