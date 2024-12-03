import turtle as t
import random
import time
import sys
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load sound
explosion_sound = pygame.mixer.Sound("boom.mp3")  # Replace with your sound file path

# Setup the screen
window = t.Screen()
window.title('ColumnD - Game Of Trons')
window.bgcolor('black')
window.setup(width=600, height=400)
window.setup(width=600, height=400)
window.cv._rootwindow.resizable(False, False)

# Global variables for player position
player_x = 0
player_y = -150

# Function to move the player to the right
def player_right():
    global player_x
    player_x += 10
    player.setx(player_x)

# Function to move the player to the left
def player_left():
    global player_x
    player_x -= 10
    player.setx(player_x)

# Function to create and move the bullet
def shoot_bullet():
    bullet = player.clone()
    bullet.shape("triangle")
    bullet.color("white")
    bullet.shapesize(stretch_wid=0.5, stretch_len=1)
    bullet.setheading(90)
    bullet.showturtle()

    # Move bullet upwards
    bullet_speed = 30
    def move_bullet():
        if bullet.ycor() < window.window_height() / 2:
            bullet.sety(bullet.ycor() + bullet_speed)
            # Check collision with enemy
            if abs(bullet.xcor() - enemy.xcor()) < 15 and abs(bullet.ycor() - enemy.ycor()) < 15:
                enemy.hideturtle()
                bullet.hideturtle()
                window.clear()

                # Play explosion sound
                explosion_sound.play()

                # Show Game Over screen
                window.bgcolor('black')
                go_turtle = t.Turtle()
                go_turtle.color('red')
                go_turtle.write("GAME OVER", align="center", font=("Arial", 36, "bold"))
                go_turtle.hideturtle()

                time.sleep(2)
                go_turtle.clear()
                go_turtle.write("Developer : Artin khodayari", align="center", font=('Arial', 24, "italic"))
                time.sleep(3)
                window.bye()
            else:
                window.ontimer(move_bullet, 50)
        else:
            bullet.hideturtle()

    move_bullet()

# Function to move enemy
def move_enemy():
    enemy_speed = 2
    new_x = enemy.xcor() + enemy_speed * enemy.direction
    if new_x > 300 or new_x < -300:
        enemy.direction *= -1
    else:
        enemy.setx(new_x)
    window.ontimer(move_enemy, 100)

# Start to listen to the keyboard
window.listen()

# Setup the player
player = t.Turtle()
player.shape('arrow')
player.color('blue')
player.penup()
player.goto(player_x, player_y)
player.setheading(90)

# Setup the enemy
enemy = t.Turtle()
enemy.shape('triangle')
enemy.color('red')
enemy.penup()
enemy.goto(0, 170)
enemy.setheading(270)
enemy.direction = 1

# Setup controls
window.onkeypress(player_right, "Right")
window.onkeypress(player_left, "Left")
window.onkeypress(shoot_bullet, "space")

# Start moving the enemy
move_enemy()

# Main loop
window.mainloop()
