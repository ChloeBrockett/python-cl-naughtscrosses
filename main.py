"""
This is a small project intended to demonstrate I have an understanding of algorithm implementation
The first version of the script will be a simple implementation of the minimax algorithm to create an opponent for a game of naughts and crosses
In future, I would like to include optimisations like alpha/beta pruning, as well as a collection of tests to prove accurate implementation and results. 
Ideally tests would be done first, but this is to demonstrate that I can implement algorithms.  
"""

import game, constant, board as gameBoard

width = constant.BOARD_WIDTH
height = constant.BOARD_HEIGHT

running =True
activeGame = False
playerTurn = True


while (running):
    turnCounter = 0
    choice=input("Do you want to play a round? y/n\n")
    if ((choice !="y") & (choice!= "n")):
        print("y or n")
    elif (choice=="n"):
        running=False
    elif (choice=="y"):
        activeGame=True
        board = gameBoard.boardInit()
        gameBoard.printBoard(board)

    while (activeGame):
        #Pre turn housekeeping
        #Check if the current board state has a winner
        winner = game.checkWin(board)
        if (winner):
            print ("Congratulations to player "+winner+"! You have won!")
            activeGame=False
            break
        #Check if the maximum number of moves have taken place and end the game in a draw if so 
        if (turnCounter>=(width*height)):
            print ("Game ends in a draw")
            activeGame=False
            break

        #Call code to handle turns 
        if (playerTurn):
            game.playerTurn(board)
              
        else:
            print ("Computer turn") 
            game.computerTurn(board)
        #Finally, render the updated board, increment the turn counter, and flip the turn controlling boolean
        gameBoard.printBoard(board)
        turnCounter +=1
        playerTurn = not playerTurn