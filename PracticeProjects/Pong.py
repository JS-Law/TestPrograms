import turtle

# Making the screen
wndw = turtle.Screen()  # assigns screen to wndw
wndw.title("Super Pong")  # calls the title method to name the title of the window
wndw.bgcolor("black")  # can use a string color
wndw.setup(width=1000, height=700, starty=None)  # calls the method .setup to define screen size and place, center
wndw.tracer(0)  # manually stops window from updating

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # speed of animation, to maximum possible speed
paddle_a.shape("square")  # assigning shape, which by default is 20p x 20p
paddle_a.color("white")  # assigning color
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # stretches width by a factor of 5 (5 * 20)
paddle_a.penup()
paddle_a.goto(-475, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # speed of animation, to maximum possible speed
paddle_b.shape("square")  # assigning shape, which by default is 20p x 20p
paddle_b.color("white")  # assigning color
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # stretches width by a factor of 5 (5 * 20)
paddle_b.penup()
paddle_b.goto(475, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)  # speed of animation, to maximum possible speed
ball.shape("square")  # assigning shape, which by default is 20p x 20p
ball.color("white")  # assigning color
ball.penup()
ball.goto(0, 0)
ball.dx = .1
ball.dy = .1  # everytime our ball moves, it moves by 2 pixels


# Functions for defining movement for Paddle A
def paddle_a_up():  # to do this we need to know the y coordinates
    y = paddle_a.ycor()  # returns the y coordinate
    y += 20  # adds 20 to y coordinate since we are moving upward
    paddle_a.sety(y)


def paddle_a_down():  # to do this we need to know the y coordinates
    y = paddle_a.ycor()  # returns the y coordinate
    y -= 20  # adds 20 to y coordinate since we are moving upward
    paddle_a.sety(y)


# Functions for defining movement for Paddle B

def paddle_b_up():  # to do this we need to know the y coordinates
    y = paddle_b.ycor()  # returns the y coordinate
    y += 20  # adds 20 to y coordinate since we are moving upward
    paddle_b.sety(y)


def paddle_b_down():  # to do this we need to know the y coordinates
    y = paddle_b.ycor()  # returns the y coordinate
    y -= 20  # adds 20 to y coordinate since we are moving upward
    paddle_b.sety(y)


# Keyboard Binding
wndw.listen()  # Listen for keyboard input
wndw.onkey(paddle_b_down, "Down")
wndw.onkey(paddle_b_up, "Up")
wndw.onkey(paddle_a_down, "s")
wndw.onkey(paddle_a_up, "w")

# Main Game Loop
# What all games are built off of(the meat and potatoes)
while True:
    wndw.update()

    # move the ball, since this is in the while loop,which is True, ball is forever adding 2 pixes to x and y axis
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    # Top Border, referencing window height
    if ball.ycor() > 340:
        ball.sety(340)
        ball.dy *= -1 # reverses direction
    if ball.ycor() < -340:
        ball.sety(-340)
        ball.dy *= -1 # reverses direction

    if ball.xcor() > 490 or ball.xcor() < -490:
        # ball.goto(0)
        ball.dx *= -1

