#Jacob Kerr
#Tic-Tac-Toe

#Database of Coordinates and Square States
coor_x = []
coor_y = []
square_state = []

#playerSelections
playerSelections = []
player0Selections = []
player1Selections = []  #the input
b = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]  #the list of correct solutions

for i in range(10):
        coor_x.append(1)
        coor_y.append(1)
        square_state.append(1)
coor_x = [False,50,150,250,50,150,250,50,150,250]
coor_y = [False,235,235,235,135,135,135,35,35,35]
for i in range(10) :
        square_state[i] = False
        #square_state : X = 1, O = -1

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

a = 0

def checkFull(lst, chosenNumber):
    for x in lst:
        if chosenNumber == lst:
            return True
    return False



def winningCheck(input):
    simNums = 0
    for x in range(8):
        for y in range(3):
            for z in range(3):
                if input[z] == b[x][y]:
                    simNums += 1
                    if simNums == 3:
                        return True
            if y == 2:
                simNums = 0
    return False

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
        playerSelections.append(1)

        #Revise square state system
        """if square_state[turn_selection] != False :
            print("This square is already full. Please select another square.")"""


        #Checking if full
        if checkFull(playerSelections) == True:
            print("This square is already full. Please select another square.")
        elif turn_selection > 9 or turn_selection < 1 :
                print("Player wins")
                break
        else :
                turtle.penup()
                turtle.goto(coor_x[turn_selection],coor_y[turn_selection])
                turtle.pendown()
                #Tile Write
                if player_turn == 0 :
                        turtle.write("X", font=("Arial", 30, "normal"),align="center")
                        #square_state[turn_selection] = -1
                        append.player0Selections()
                        player_turn = 1
                elif player_turn == 1 :
                        turtle.write("O", font=("Arial", 30, "normal"),align="center")
                        #square_state[turn_selection] = 1
                        player_turn = 0
                else :
                        print("Error! Shutting down program!")
#Hello world
