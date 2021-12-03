import turtle
import pandas

from dot import Dot
from init import screen
from scoreboard import Scoreboard


data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()

screen.title('U.S. States Game')
screen.setup(width=800, height=600)
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

scoreboard = Scoreboard()

while scoreboard.score > 0:
	answer = screen.textinput(title='Title Here', prompt='Make your answer').strip().title()
	
	if answer == 'Exit':
		missing_states = pandas.DataFrame(all_states)
		missing_states.to_csv('states_to_learn.csv')
		break
		
	scoreboard.tries += 1
	scoreboard.refresh()
	if answer in all_states:
		all_states.remove(answer)
		scoreboard.add_point()
		position = data[data.state == answer]
		dot = Dot()
		dot.move(answer, int(position.x), int(position.y))
