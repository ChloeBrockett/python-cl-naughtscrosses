"""
This is a small project intended to demonstrate I have an understanding of algorithm implementation
The first version of the script will be a simple implementation of the minimax algorithm to create an opponent for a game of naughts and crosses
In future, I would like to include optimisations like alpha/beta pruning, as well as a collection of tests to prove accurate implementation and results. 
Ideally tests would be done first, but this is to demonstrate that I can implement algorithms.  
"""

import game, constant

playerPiece = constant.PLAYER1_SYMBOL
computerPiece = constant.PLAYER2_SYMBOL

running =True
activeGame = False
playerTurn = True


while (running):
    choice=input("Do you want to play a round? y/n\n")
    if ((choice !="y") & (choice!= "n")):
        print("y or n")
    elif (choice=="n"):
        running=False
    elif (choice=="y"):
        activeGame=True
        board = game.boardInit()

    while (activeGame):
        if (playerTurn):
            board = game.playerTurn(board)
            board = [["a","b","c"],["d","e","f"],["g","h","i"]]
            game.printBoard(board)
            game.checkWin(board,playerPiece)
