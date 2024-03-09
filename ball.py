from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")  # Set the shape to a circle
        self.shapesize(stretch_wid=2, stretch_len=2)  # Set the width and height
        self.penup()  # Lift the pen to avoid drawing lines
        self.goto(0, 0)  # Set initial position
        self.color("white")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

        # Bounce if the ball hits the top or bottom wall
        if new_y > 290 or new_y < -290:
            self.bounce_y()

    def bounce_y(self):
        self.y_move *= -1
