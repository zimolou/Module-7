import turtle
import random
import time

screen = turtle.Screen()
screen.title("Turtle Racing")
screen.bgcolor("lightgreen")
screen.setup(width=600, height=600)
screen.tracer(0)

player = turtle.Turtle()
player.shape("square")
player.color("blue")
player.shapesize(stretch_wid=1, stretch_len=2)
player.penup()
player.goto(0, -250)

enemies = []
for _ in range(5):
    enemy = turtle.Turtle()
    enemy.shape("square")
    enemy.color("red")
    enemy.shapesize(stretch_wid=1, stretch_len=2)
    enemy.penup()
    x = random.randint(-280, 280)
    y = random.randint(200, 400)
    enemy.goto(x, y)
    enemies.append(enemy)

def move_left():
    x = player.xcor()
    if x > -280:
        x -= 20
    player.setx(x)

def move_right():
    x = player.xcor()
    if x < 280:
        x += 20
    player.setx(x)

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

score = 0
game_over = False
speed = 5

score_display = turtle.Turtle()
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font=("Arial", 20, "normal"))

while not game_over:
    screen.update()
    
    for enemy in enemies:
        y = enemy.ycor()
        y -= speed
        enemy.sety(y)
        
        if abs(player.xcor() - enemy.xcor()) < 30 and abs(player.ycor() - enemy.ycor()) < 20:
            game_over = True
            score_display.clear()
            score_display.write(f"Game Over! Final Score: {score}", align="center", font=("Arial", 20, "normal"))
        
        if enemy.ycor() < -300:
            x = random.randint(-280, 280)
            y = random.randint(300, 400)
            enemy.goto(x, y)
            score += 1
            score_display.clear()
            score_display.write(f"Score: {score}", align="center", font=("Arial", 20, "normal"))
    
    time.sleep(0.05)

turtle.done()

