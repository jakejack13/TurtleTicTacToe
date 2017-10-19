#Jacob Kerr
#Tic-Tac-Toe

#Database of Coordinates
Coor1_x = 100
Coor1_y = -100
Coor2_x = False
Coor2_y = False
Coor3_x = False
Coor3_y = False
Coor4_x = False
Coor4_y = False
Coor5_x = False
Coor5_y = False
Coor6_x = False
Coor6_y = False
Coor7_x = False
Coor7_y = False
Coor8_x = False
Coor8_y = False

import turtle
turtle.hideturtle()
#Make square
turtle.goto(300, 0)
turtle.goto(300, 300)
turtle.goto(0, 300)
turtle.goto(0, 0)

#Make grid
turtle.goto(0,100)
turtle.goto(300,100)
turtle.goto(300,200)
turtle.goto(0,200)
turtle.goto(0,300)
turtle.goto(100,300)
turtle.goto(100,0)
turtle.goto(200,0)
turtle.goto(200,300)

#X = 0, O = 1
#First time playthrough set up
PlayerTurn = 0
PlayState = 1

#Play Loop
for PlayState in range(1)
TurnSelection = int(input("Please select the number of the square to play your tile: "))
turtle.goto(Coor[TurnSelection]_x,Coor[TurnSelection]_y)
#if PlayerTurn == 0 :
	