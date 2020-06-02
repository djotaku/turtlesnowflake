"""This is a snowflake program made by Samuel and Daddy on June 2 2020"""

import turtle
import random

slow_poke = turtle.Turtle()
slow_poke.color("forest green")
turtle.Screen().bgcolor("honeydew2")
for i in range(10):
    for i in range(2):
        slow_poke.forward(100)
        slow_poke.right(60)
        slow_poke.forward(100)
        slow_poke.right(120)
    slow_poke.right(36)

turtle.mainloop()
