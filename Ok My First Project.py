# Create Game on "turtle" Library
import turtle

# background wind
wind = turtle.Screen()
wind.title("Ping&Pong")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

# hand1
hand1 = turtle.Turtle()
hand1.speed(0)
hand1.shape("square")
hand1.color("blue")
hand1.shapesize(stretch_wid=5, stretch_len=1)
hand1.penup()
hand1.goto(-350, 0)

# hand2
hand2 = turtle.Turtle()
hand2.speed(0)
hand2.shape("square")
hand2.color("red")
hand2.shapesize(stretch_wid=5, stretch_len=1)
hand2.penup()
hand2.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1   # Changing the speed of a game to the x axis
ball.dy = 0.1   # Changing the speed of a game to the x axis

# score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("PlayerBlue: 0 PlayerRed: 0", align="center", font=("Courier", 24, "normal"))


# function
def hand1_up():
    y = hand1.ycor()
    y += 20
    hand1.sety(y)


def hand1_down():
    y = hand1.ycor()
    y -= 20
    hand1.sety(y)


def hand2_up():
    y = hand2.ycor()
    y += 20
    hand2.sety(y)


def hand2_down():
    y = hand2.ycor()
    y -= 20
    hand2.sety(y)


# keyboard bindings
wind.listen()
wind.onkeypress(hand1_up, "w")
wind.onkeypress(hand1_down, "s")
wind.onkeypress(hand2_up, "Up")
wind.onkeypress(hand2_down, "Down")

# main Game Loop
while True:
    wind.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("PlayerBlue: {} PlayerRed: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("PlayerBlue: {} PlayerRed: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    # collision hand and ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < hand2.ycor() + 40 and ball.ycor() > hand2.ycor() - 40):
        ball.sety(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < hand1.ycor() + 40 and ball.ycor() > hand1.ycor() - 40):
        ball.sety(-340)
        ball.dx *= -1
