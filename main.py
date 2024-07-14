import colorgram
from turtle import Turtle, Screen
import random


Screen().setup(500, 400)
choice = Screen().textinput('choice', "Choose your turtle's color:(from rainbow color list):" )

# timmy.color(choice)
# timmy.penup()
# timmy.goto(x=-230, y=-100)

colors = ['orange', 'red', 'blue', 'green', 'yellow', 'purple']
y = -140
turtles = []
for i in range(0, len(colors)):
    turtle = Turtle('turtle')
    turtles.append(turtle)
    turtle.penup()
    turtle.color(colors[i])
    turtle.goto(x=-230, y=y)
    y += 60


game = True
while game:
    for i in range(len(turtles)):
        turtles[i].forward(random.randint(0, 10))
        if turtles[i].xcor() >= 230:
            game = False
            color = turtles[i].color()
if color[0].lower() == choice.lower():
    print(f'{color[0].capitalize()} turtle won the race. You won! ')
else:
    print(f'{color[0].capitalize()} turtle won the race. You lost. ')

Screen().exitonclick()
