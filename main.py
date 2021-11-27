import random
from turtle import Turtle, Screen


turtle_color = ['green', 'red', 'brown', 'purple', 'yellow', 'blue']
y_start_position_shift = 40
turtles_list = []
is_start = False

screen = Screen()
screen.setup(width=500, height=400)

user_choice = screen.textinput(title='Your bet', prompt='Green, Red, Purple, Yellow, Blue, Brown').lower()

for item in turtle_color:
    tim = Turtle(shape='turtle')
    tim.penup()
    tim.color(item)
    tim.goto(x=-240, y=-140 + y_start_position_shift)
    y_start_position_shift += 40
    turtles_list.append(tim)

if user_choice:
    is_start = True

while is_start:
    for turtle in turtles_list:
        if turtle.xcor() > 230:
            win_colour = turtle.pencolor()
            if win_colour == user_choice:
                print('You won!')
            else:
                print(f'You loose! The colour of winning turtle is {win_colour}.')
            is_start = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
