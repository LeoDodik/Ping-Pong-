from turtle import Turtle
from paddle import Paddle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")  # Set the shape to a circle
        self.shapesize(stretch_wid=1, stretch_len=1)  # Set the width and height
        self.penup()  # Lift the pen to avoid drawing lines
        self.goto(0, 0)  # Set initial position
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

        # Bounce if the ball hits the top or bottom wall
        if new_y > 290 or new_y < -290:
            self.bounce_y()

    def increase_speed(self):
        self.speed("fastest")

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
    def restart(self):
        self.goto(0,0)
        self.bounce_x()
