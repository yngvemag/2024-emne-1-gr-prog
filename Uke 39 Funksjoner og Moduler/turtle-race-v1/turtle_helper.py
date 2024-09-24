import turtle


# en funksjon som lager en turtle og returerer denne
# den skal form som skilpadde og en farge.
def create_turtle(color: str) -> turtle.Turtle:
    t = turtle.Turtle()
    t.color(color)
    t.shape('turtle')
    return t


def draw_vertical_line(t: turtle.Turtle,
                       pos: tuple[int, int], height: int) -> None:

    # (x, y) = (-300, -300)
    t.penup()
    t.goto(pos[0], pos[1])
    t.left(90)
    t.pendown()
    t.forward(height)
