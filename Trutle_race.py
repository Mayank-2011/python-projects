from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width = 500, height = 400)

is_race_on = False
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
color = ['purple', 'blue', 'green', 'yellow', 'orange', 'red']

y_position = [-100, -60, -20, 20, 60, 100]
all_turtles = []
for i in range(6):
    new_turtle= Turtle('turtle')
    new_turtle.penup()
    new_turtle.goto(x=-230, y= y_position[i])
    new_turtle.color(color[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtles in all_turtles:
        if turtles.xcor() > 230:
            is_race_on = False
            winning_color = turtles.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")
        distance = random.randint(0,10)
        turtles.forward(distance)

screen.exitonclick()
