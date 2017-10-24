#Jacob Kerr
#Tic-Tac-Toe

#Database of Coordinates and Square States
CoorX = []
CoorY = []
SquareState = []
for i in range(10):
        CoorX.append(1)
        CoorY.append(1)
        SquareState.append(1)
CoorX[1] = 50
CoorY[1] = 250
CoorX[2] = 150
CoorY[2] = 250
CoorX[3] = 250
CoorY[3] = 250
CoorX[4] = 50
CoorY[4] = 150
CoorX[5] = 150
CoorY[5] = 150
CoorX[6] = 250
CoorY[6] = 150
CoorX[7] = 50
CoorY[7] = 50
CoorX[8] = 150
CoorY[8] = 50
CoorX[9] = 250
CoorY[9] = 50
for i in range(10) :
        SquareState[i] = False

#Turtle Time
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
while(PlayState == 1):
        #Player Message
        if PlayerTurn == 0 :
                print("Player X's turn")
        elif PlayerTurn == 1 :
                print("Player O's turn")
        else:
                print("Error! Shutting down program!")
                break
        #Square Selection
        TurnSelection = int(input("Please select the number of the square to play your tile: "))
        if TurnSelection > 9 or TurnSelection < 1 :
                print("Player wins")
                break
        turtle.penup()
        turtle.goto(CoorX[TurnSelection],CoorY[TurnSelection])
        turtle.pendown()
        #Tile Write
        if PlayerTurn == 0 :
                turtle.write("X", font=("Arial", 30, "normal"),align="center")
                SquareState[TurnSelection] = 0
                PlayerTurn = 1
        elif PlayerTurn == 1 :
                turtle.write("O", font=("Arial", 30, "normal"),align="center")
                SquareState[TurnSelection] = 1
                PlayerTurn = 0
        else :
                print("Error! Shutting down program!")
        #Check Win Conditions (Needs to be debugged - Returns win after first turn)
        if ((SquareState[1] == 0 and SquareState[2] == 0 and SquareState[3] == 0) or (SquareState[4] == 0 and SquareState[5] == 0 and SquareState[6] == 0) or (SquareState[7] == 0 and SquareState[8] == 0 and SquareState[9] == 0) or (SquareState[1] == 0 and SquareState[4] == 0 and SquareState[7] == 0) or (SquareState[2] == 0 and SquareState[5] == 0 and SquareState[8] == 0) or (SquareState[3] == 0 and SquareState[6] == 0 and SquareState[9] == 0) or (SquareState[1] == 0 and SquareState[5] == 0 and SquareState[9] == 0) or (SquareState[3] == 0 and SquareState[5] == 0 and SquareState[7] == 0)) :
                print("Player X won!")
                break
        elif ((SquareState[1] == 1 and SquareState[2] == 1 and SquareState[3] == 1) or (SquareState[4] == 1 and SquareState[5] == 1 and SquareState[6] == 1) or (SquareState[7] == 1 and SquareState[8] == 1 and SquareState[9] == 1) or (SquareState[1] == 1 and SquareState[4] == 1 and SquareState[7] == 1) or (SquareState[2] == 1 and SquareState[5] == 1 and SquareState[8] == 1) or (SquareState[3] == 1 and SquareState[6] == 1 and SquareState[9] == 1) or (SquareState[1] == 1 and SquareState[5] == 1 and SquareState[9] == 1) or (SquareState[3] == 1 and SquareState[5] == 1 and SquareState[7] == 1)) :
                print("Player O won!")
                break
        else :
                print("Nice play!")
