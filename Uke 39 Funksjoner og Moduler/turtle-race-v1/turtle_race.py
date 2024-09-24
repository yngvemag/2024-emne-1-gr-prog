import turtle
import random as rnd
from turtle_helper import *

COLORS = ('yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan',
          'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray')
NR_OF_PLAYERS = 2

players: list[turtle.Turtle] = []


def game_setup():
    # Vi trenger 2 skilpadder
    for i in range(NR_OF_PLAYERS):
        col = COLORS[i]
        players.append(create_turtle(col))

    # tegne opp brettet - trenger en turtle som gjør jobben
    setup_turtle = create_turtle('blue')
    draw_vertical_line(setup_turtle, (-300,-300), 600)




if __name__ == '__main__':
    game_setup()

turtle.exitonclick()
