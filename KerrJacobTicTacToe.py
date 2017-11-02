#Jacob Kerr
#Tic-Tac-Toe

#Database of Coordinates and Square States
coor_x = []
coor_y = []
square_state = []
for i in range(10):
        coor_x.append(1)
        coor_y.append(1)
        square_state.append(1)
coor_x = [False,50,150,250,50,150,250,50,150,250]
coor_y = [False,235,235,235,135,135,135,35,35,35]
for i in range(10) :
        square_state[i] = False
player_turn
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
player_turn = 0
play_state = 1
#Play Loop
while(play_state == 1):
        #Player Message and Turn Selection
        if player_turn == 0 :
                print("Player X's turn")
        elif player_turn == 1 :
                print("Player O's turn")
        else:
                print("Error! Shutting down program!")
                break
        #Square Selection
        turn_selection = int(input("Please select the number of the square to play your tile: "))
        if not square_state[turn_selection]:
                print("This square is already full. Please select another square.")
        if turn_selection > 9 or turn_selection < 1 :
                print("Player wins")
                break
        turtle.penup()
        turtle.goto(coor_x[turn_selection],coor_y[turn_selection])
        turtle.pendown()
        #Tile Write
        if player_turn == 0 :
                turtle.write("X", font=("Arial", 30, "normal"),align="center")
                square_state[turn_selection] = 0
                player_turn = 1
        elif player_turn == 1 :
                turtle.write("O", font=("Arial", 30, "normal"),align="center")
                square_state[turn_selection] = 1
                player_turn = 0
        else :
                print("Error! Shutting down program!")
        #Check Win Conditions (Needs to be debugged - Returns win after first turn)
        #if ((square_state[1] == 0 and square_state[2] == 0 and square_state[3] == 0) or (square_state[4] == 0 and square_state[5] == 0 and square_state[6] == 0) or (square_state[7] == 0 and square_state[8] == 0 and square_state[9] == 0) or (square_state[1] == 0 and square_state[4] == 0 and square_state[7] == 0) or (square_state[2] == 0 and square_state[5] == 0 and square_state[8] == 0) or (square_state[3] == 0 and square_state[6] == 0 and square_state[9] == 0) or (square_state[1] == 0 and square_state[5] == 0 and square_state[9] == 0) or (square_state[3] == 0 and square_state[5] == 0 and square_state[7] == 0)) :
        #        print("Player X won!")
        #        break
        #elif ((square_state[1] == 1 and square_state[2] == 1 and square_state[3] == 1) or (square_state[4] == 1 and square_state[5] == 1 and square_state[6] == 1) or (square_state[7] == 1 and square_state[8] == 1 and square_state[9] == 1) or (square_state[1] == 1 and square_state[4] == 1 and square_state[7] == 1) or (square_state[2] == 1 and square_state[5] == 1 and square_state[8] == 1) or (square_state[3] == 1 and square_state[6] == 1 and square_state[9] == 1) or (square_state[1] == 1 and square_state[5] == 1 and square_state[9] == 1) or (square_state[3] == 1 and square_state[5] == 1 and square_state[7] == 1)) :
        #        print("Player O won!")
        #        break
        #else :
        #        print("Nice play!")
#Hello world
