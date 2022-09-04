from turtle import Screen
from player import Player
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("My Pong Game")
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0)
is_game_on = True    
scoreboard = Scoreboard()


l_player = Player((-350,0))
r_player = Player((350,0))
ball = Ball()
ball.speed(1)

screen.listen()
screen.onkeypress(r_player.go_up,"Up")
screen.onkeypress(r_player.go_down,"Down")
screen.onkeypress(l_player.go_up,"w")
screen.onkeypress(l_player.go_down,"s")      



while is_game_on:
    time.sleep(0.08)
    screen.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    if ball.distance(r_player) < 50 and ball.xcor() > 320 or ball.distance(l_player) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.goes_out()
        ball.opposite_direction()
        
    
    if ball.xcor() > 380:
        scoreboard.increase_l_score()
        
    elif ball.xcor() < -380:
        scoreboard.increase_r_score()







screen.exitonclick()