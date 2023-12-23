import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0


# Set up the screen
wn = turtle.Screen()
wn.title("Snake game by Vivian")
wn.bgcolor("light green")
wn.setup(width = 600, height = 600)
wn.tracer(0) 
# wn.tracer = desliga as atualizações


# Criando a cabeça da cobrinha
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("dark green")
head.penup()
head.goto(0,0)
head.direction = "stop"

# FOOD
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("orange")
food.penup()
food.goto(0,100)
food.direction = "stop"

# Fazendo a cobra crescer
segments = []

# PEN
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0   High score: 0", align="center", font=("Arial", 20, "normal"))


# Funções
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"


def move():
    if head.direction == "up":
        y  = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y  = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x  = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x  = head.xcor()
        head.setx(x - 20)


# Key boards bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


# Main game loop
while True:
    wn.update()

    # Verificando a colisão com a borda
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000,1000)
        
        # Limpando o segmento de lista
        segments.clear()

        # Reset the delay
        delay = 0.1

        # Zerar score
        score = 0
        # Update the score display
        pen.clear()
        pen.write("Score: {}   High score: {}".format(score, high_score), align="center", font=("Arial", 20, "normal"))

    # Colisão com a comida
    if head.distance(food) < 20:
        # Mover a comida em outro lugar aleatório
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Adicionar um segmento
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("dark green")
        new_segment.penup()
        segments.append(new_segment)

        # Increase the score
        score  += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}   High score: {}".format(score, high_score), align="center", font=("Arial", 20, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)


    move()

    # Colisão com o corpo
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

    time.sleep(delay)

wn.mainloop()
