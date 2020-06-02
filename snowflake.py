"""This is a snowflake program made by Samuel and Daddy on June 2 2020"""

import turtle
import random

slow_poke = turtle.Turtle()
slow_poke.color("forest green")
turtle.Screen().bgcolor("honeydew2")
colors = ["forest green", "HotPink1", "black", "sienna4"]

slow_poke.penup()
slow_poke.forward(90)
slow_poke.left(45)
slow_poke.pendown()

def branch():
    for i in range(3):
        for i in range(3):
             slow_poke.forward(30)
             slow_poke.backward(30)
             slow_poke.right(45)
        slow_poke.left(90)
        slow_poke.backward(30)
        slow_poke.left(45)
    slow_poke.right(90)
    slow_poke.forward(90)

for i in range(8):
    branch()
    slow_poke.left(45)

turtle.mainloop()
