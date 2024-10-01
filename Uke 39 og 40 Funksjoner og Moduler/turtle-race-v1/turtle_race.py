import turtle
import random as rnd
from turtle_helper import *

COLORS = ('darkgreen', 'skyblue', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'gold', 'cyan',
          'turquoise', 'lightgreen', 'green', 'yellow', 'chocolate', 'brown', 'black', 'gray')
NR_OF_PLAYERS = 2

players: list[turtle.Turtle] = []


def game_setup():
    # Vi trenger 2 skilpadder
    #for i in range(NR_OF_PLAYERS):
    #    col = COLORS[i]
    #    players.append(create_turtle(col))

    # list-comprehension
    players = [create_turtle(COLORS[i]) for i in range(NR_OF_PLAYERS)]

    # tegne opp brettet - trenger en turtle som gjør jobben
    setup_turtle = create_turtle('blue')
    draw_vertical_line(setup_turtle, (-300, -300), 600)
    write_text(setup_turtle, 'START', (-310, 310))
    draw_vertical_line(setup_turtle, (300, -300), 600)
    write_text(setup_turtle, 'END', (290, 310))
    setup_turtle.hideturtle()

    # Plassere spiller bak start streken.
    set_players_ready(players, -300, 600)


if __name__ == '__main__':
    game_setup()

turtle.exitonclick()
