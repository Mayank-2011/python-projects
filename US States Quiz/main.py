import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)
correct_state_count = 0
correct_guess = []
states = pandas.read_csv('50_states.csv')
states_list = states.state.to_list()

while len(correct_guess) < 50:
    answer = screen.textinput(title=f"{len(correct_guess)}/50 States Correct", prompt="What's another state name?").title()
    if answer == "Exit":
        states_to_learn = []
        for state in states_list:
            if state in correct_guess:
                continue
            else:
                states_to_learn.append(state)

        new_dict = {'States to learn': states_to_learn}

        df = pandas.DataFrame(new_dict)
        df.to_csv('states_to_learn.csv')
        break
    if answer in states_list:
        correct_guess.append(answer)
        writer = turtle.Turtle()
        writer.hideturtle()
        x_cor = int(states[states['state'] == f"{answer}"].x)
        y_cor = int(states[states['state'] == f"{answer}"].y)
        writer.penup()
        writer.goto(x_cor, y_cor)
        writer.write(f"{answer}", align="center", font=("courier", 10, "normal"))
