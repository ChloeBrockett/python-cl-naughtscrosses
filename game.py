#This is the file containing the logic for the game
import copy
import board as gameBoard

import constant
whitespace = constant.EMPTY_SQUARE
height = constant.BOARD_HEIGHT
width=constant.BOARD_WIDTH
playerPiece = constant.PLAYER1_SYMBOL
computerPiece = constant.PLAYER2_SYMBOL

#function to check if a specified player has won.
#Should currently be expandable to all square sized boards where the win condition is a full line.
#Given a board, checks all possible lines for a winner. Returns the first winning piece, or None if no winner found
def checkWin (board):
    #A player wins if they get a complete line. This means checking each column, each row, and both diagonals
    
    lines = gameBoard.getLines(board)
    #Now that we have all the lines. 
    for line in lines:
        if ( (len(set(line)) == 1) & (line [0] != whitespace) ):
            return line[0]
    #If a winner was not found in the list of lines, return None    
    return None

#Function to ask the player to input a move. Returns a validated move as an row col tuple
def playerGetMoveInput(board):
    inputtingMove = True
    while (inputtingMove):
        row = (input("Please enter the row for your move: "))
        col = (input("Please enter the column for your move: "))
        print ("You have entered ("+str(row)+","+str(col)+")")
        confirm =input ("Please confirm choice (y/n): ")
        if ((confirm !="y") & (confirm!= "n")):
            print ("Please enter y or n: ")
        elif (confirm=="n"):
            print ("Please re-enter your move")
        elif (confirm=="y"):
                inputtingMove=False
          
    return (row,col)

#minimax algorithm for finding the best move. 
def minimax(board,maximisingPlayer,maximisingPlayersPiece,minimisingPlayersPiece):
    #We need to check if the node is a terminal node. 
    #The game ends when the board is full, or if a player has won
    winner = checkWin(board)
    empties = gameBoard.findEmptySquares(board)
    #If there are no empty squares, then the game has ended in a draw and we should give the node a net score of 0
    if (len(empties)==0):
        return (0,None)
    
    #If the winner is the player we care about maximising for, then return a positive score
    #If the winner is not the player we care about, then return a negative score
    if (winner==maximisingPlayersPiece):
        return (1,None)
    elif (winner):
        return (-1,None)

    #If we have not reached a terminal node, we should continue to traverse our tree. 
    if (maximisingPlayer):
        #Here we are the player picking the move that maximises their shot at winning, so we initialise our score
        #to an arbitrarily huge negative number
        bestScore = -1000
        bestMove = None
        #We should then generate children nodes using the list of empties we have
        #It is the maximising players turn so we use their piece
        #First we need to copy the existing board without a reference so we can modify it, then we can create a child 
        #where the computer plays each empty square
        children = []
        for i in range(0,len(empties)):
            children.append(copy.deepcopy(board))
            gameBoard.setBoardSquare(children[i],empties[i][0],empties[i][1],maximisingPlayersPiece)
        for i in range(0,len(children)):
            score = max(bestScore,  minimax(children[i],False,maximisingPlayersPiece,minimisingPlayersPiece)[0])
            if score>bestScore:
                bestScore=score
                bestMove=empties[i]

        return (score,bestMove)
    else:
        #We want to do the opposite of the above
        bestScore = 1000
        bestMove=None
        children = []
        for i in range(0,len(empties)):
            children.append(copy.deepcopy(board))
            gameBoard.setBoardSquare(children[i],empties[i][0],empties[i][1],minimisingPlayersPiece)
        for i in range(0,len(children)):
            score = min(bestScore,minimax(children[i],True,maximisingPlayersPiece,minimisingPlayersPiece)[0])
            if score<bestScore:
                bestScore=score
                bestMove=empties[i]

        return (score,bestMove)
        

#Function that handles the logic for the players turn. 
def playerTurn(board):
    processingMove = True
    while (processingMove):
        #First we need to get the input from the player
        (row,col) = playerGetMoveInput(board)
        #Check the input is an integer
        if not(row.isdigit()  &  col.isdigit()):
            print("Please only enter valid integers")
            continue
        row = int(row)
        col = int (col)
        if not ((row in range(0,height)) & (col in range(0,width))):
            print ("You placed your piece off the board, try again")
            continue
        #Check that the square is empty. Only allow a move to proceed if it is
        if (gameBoard.checkSquareEmpty(board,row,col)):
            processingMove=False
        else: 
            print ("The square was not empty")

    #Once we have the input we can put it on the board
    board = gameBoard.setBoardSquare(board,row,col,playerPiece)
    return (board)

#Function that handles the logic for the computers turn
def computerTurn(board):
    currentBoard = board
    bestMove = minimax(currentBoard,True,computerPiece,playerPiece)[1]
    gameBoard.setBoardSquare(board,bestMove[0],bestMove[1],computerPiece)
    return board

