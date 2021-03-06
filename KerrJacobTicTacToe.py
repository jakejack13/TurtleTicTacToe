#Jacob Kerr
#кai typявнський
#Tic-Tac-Toe

#Database of Coordinates and Square States
coor_x = []
coor_y = []
square_state = []

#playerSelections
playerSelections = []
player0Selections = []
player1Selections = [] #the input
winningCombinations = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]] #the list of correct solutions

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
turtle.screensize(1920,1080)
turtle.speed("fastest")
turtle.hideturtle()
turtle.screensize(1920,1080)
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

def checkFull(input, chosenNumber):
    for x in input:
        if chosenNumber == x:
            return True
    return False

hPlayer = "O"
cPlayer = "X"

#Returns list of empty spaces
def emptyIndexes(board) :
    newBoard = []
    for i in board :
        if i != "O" and i != "X" :
            newBoard.append(i)
    return newBoard

#Checks win conditions
def checkWin(board, player) :
    if (board[0] == player and board[1] == player and board[2] == player) or (board[3] == player and board[4] == player and board[5] == player) or (board[6] == player and board[7] == player and board[8] == player) or (board[0] == player and board[3] == player and board[6] == player) or (board[1] == player and board[4] == player and board[7] == player) or (board[2] == player and board[5] == player and board[8] == player) or (board[0] == player and board[4] == player and board[8] == player) or (board[2] == player and board[4] == player and board[6] == player) :
        return True
    else:
        return False

#Minimax algorithm
def minMax(newBoard, player) :
    availSpots = emptyIndexes(newBoard)
    #Checking win conditions and returning score if met
    if checkWin(newBoard,hPlayer) :
        return {"score":-10}
    elif checkWin(newBoard, cPlayer) :
        return {"score":10}
    elif len(availSpots) == 0 :
        return {"score":0}
    moves = []
    #Looping through possible moves in each space
    for i in range(len(availSpots)) :
        move = {
            "index":None,
            "score":None
        }
        move["index"] = newBoard[availSpots[i]]
        newBoard[availSpots[i]] = player
        if (player == cPlayer) :
            #Recursion to check all possible moves
            result = minMax(newBoard, hPlayer)
            move["score"] = result["score"]
        else :
            result = minMax(newBoard, cPlayer)
            move["score"] = result["score"]
        #Replacing lost element and adding potential move to list
        newBoard[availSpots[i]] = move["index"]
        moves.append(move)
    #Checking best possible move from move list
    if player == cPlayer :
        bestScore = -10000
        for i in range(len(moves)) :
            if moves[i]["score"] > bestScore :
                bestScore = moves[i]["score"]
                bestMove = i
    else :
        bestScore = 10000
        for i in range(len(moves)) :
            if moves[i]["score"] < bestScore :
                bestScore = moves[i]["score"]
                bestMove = i
    return moves[bestMove]

def winningCheck(input):
    simNums = 0
    if len(input) < 3:
        return False
    for x in range(8):
        for y in range(3):
            for z in range(len(input)):
                if input[z] == winningCombinations[x][y]:
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
                turn_selection = int(input("Please select the number of the square to play your tile: "))
        elif player_turn == 1 :
                print("Player O's turn")
                turn_selection = int(input("Please select the number of the square to play your tile: "))
        else:
                print("Error! Shutting down program!")
                break
        #Square Selection

        #Revise square state system


        #Checking if full
        if checkFull(playerSelections, turn_selection) == True:
            print("This square is already full. Please select another square.")
        elif turn_selection == "":
            print("You didn't chose a square")
        elif turn_selection > 9 or turn_selection < 1 :
                print("Player wins")
                break
        else :
                playerSelections.append(turn_selection)
                turtle.penup()
                turtle.goto(coor_x[turn_selection],coor_y[turn_selection])
                turtle.pendown()
                #Tile Write
                if player_turn == 0 :
                        turtle.write("X", font=("Arial", 30, "normal"),align="center")
                        #square_state[turn_selection] = -1
                        player0Selections.append(turn_selection)
                        if winningCheck(player0Selections) == True:
                            print('Player X won!')
                            play_state = 0
                        player_turn = 1
                elif player_turn == 1 :
                        turtle.write("O", font=("Arial", 30, "normal"),align="center")
                        #square_state[turn_selection] = 1
                        player1Selections.append(turn_selection)
                        if winningCheck(player1Selections) == True:
                            print('Player O won!')
                            play_state = 0
                        player_turn = 0
                else :
                        print("Error! Shutting down program!")
#Hell world
