import turtle

my_turtle = turtle.Turtle()
my_turtle.color('blue')
my_turtle.shape('turtle')
my_turtle.speed(100)


# Lage en funksjon som tegner et kvadrat
# Plan
#   1. Name: 'draw_square'
#   2. Parameter(e): vi må ha en lengde paramter: type 'int', color -> type: str
#   3. Return ? -> Trenger ingen return -> None
def draw_square(length: int, color: str = 'yellow') -> None:
    my_turtle.fillcolor(color)
    my_turtle.begin_fill()

    for _ in range(4):
        my_turtle.forward(length)
        my_turtle.left(90)

    my_turtle.end_fill()


# Plan
#   1. Navn: draw_triangle
#   2. Parametere: lengde -> int
#   3. Return -> None
def draw_triangle(length: int) -> None:
    for _ in range(3):
        my_turtle.forward(length)
        my_turtle.left(120)


my_turtle.fillcolor('red')
my_turtle.begin_fill()
draw_square(100)
my_turtle.end_fill()

# plan
# start verdi: 50
# step: 50
# stop: 301
colors = ['red', 'yellow', 'green', 'blue', 'purple', 'cyan', 'white']
j = 0
for i in range(300, 30, -50):
    draw_square(i, colors[j])
    j += 1



turtle.exitonclick()
