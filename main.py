import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)
def turtle_left():
    turtle_instance.setheading(turtle_instance.heading()-100)
def turtle_right():
    turtle_instance.setheading(turtle_instance.heading()+100)
def clear_screen():
    turtle_instance.clear()
def turtle_pen_up():
    turtle_instance.penup()
def turtle_pen_down():
    turtle_instance.pendown()
def turtle_return_home():
    turtle_instance.home()

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward,key="space")
drawing_board.onkey(fun=turtle_left,key="a")
drawing_board.onkey(fun=turtle_right,key="d")
drawing_board.onkey(fun=clear_screen,key="c")
drawing_board.onkey(fun=turtle_pen_up,key="q")
drawing_board.onkey(fun=turtle_pen_down,key="e")
drawing_board.onkey(fun=turtle_return_home,key="h")

turtle.mainloop()