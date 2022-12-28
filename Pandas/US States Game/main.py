import turtle
import pandas
from name_states import NameStates

def target_state_coordinate(name_states):
    location = data[data.state == name_states]
    x_coord = int(location.x)
    y_coord = int(location.y)
    position = (x_coord, y_coord)
    return position

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

namestate = NameStates()

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

correct_states = 0
while correct_states < 50:
    user_guess = screen.textinput(title = f"{correct_states}/50 States Correct",
                                  prompt = "What's another state name?").title()
    if user_guess == 'Exit':
        break
    if user_guess in states:
        position = target_state_coordinate(user_guess)
        namestate.show_up(position, user_guess)
        correct_states += 1
        states.remove(user_guess)

df = pandas.DataFrame(states)
df.to_csv("states_to_learn.csv")