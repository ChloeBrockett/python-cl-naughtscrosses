#This file contains the logic for manipulating the game board 

import constant
whitespace = constant.EMPTY_SQUARE
height = constant.BOARD_HEIGHT
width=constant.BOARD_WIDTH
playerPiece = constant.PLAYER1_SYMBOL
computerPiece = constant.PLAYER2_SYMBOL

#Initialise a game board and return it. 
def boardInit():
    board =  [[whitespace for x in range(width)] for y in range(height)]
    return board

#Given a board state, return a list of all empty (row, col) coordinate tuples
def findEmptySquares(board):
    empties = []
    for row in range(0,len(board)):
        for col in range (0,len(board[row])):
            if (board[row][col] == whitespace):
                empties.append((row,col))
    return empties

#Given a game board, print the current game state in a human readable manner.
def printBoard(board):
    print ("The current game board")
    colHeads = [range(0,width)[x] for x in range(0,width) ]
    rowHeads = [range(0,height)[x] for x in range(0,height) ]
    seperator = "|"
    #we want a horizontal divider between each line of the board. It would be neat to have the length calculated programatically
    #this allows for us changing the board size later
    #We know there will always be three characters worth of space between the left margin and the start of where the line should be drawn
    #each element in a row will need a line under it, and there will be (row length - 1) divider characters
    #therefore the first three chacters will be three spaces, and then there will be (2*width-1) line characters

    dividerLine = "   "+("-"*(2*width-1))
    
    #print the first row, which will be just the column numbers 
    print ("  ",*colHeads, sep=" " )

    for row in rowHeads:

        print (str(row)+" ",seperator.join(e for e in board[row]))
        #after each line, print the divider, unless its the last line (like a real board on paper)
        #account for 0 indexing
        if (not (row==height-1)):
            print (dividerLine)
    print()

#Helper function that checks if a square is empty. Returns a bool if so
def checkSquareEmpty(board,row,col):
    if (board[row][col]==whitespace):
        return True
    else:
        return False

#Helper function that sets a square to the specified piece. Returns the new board 
def setBoardSquare(board,row,col,piece):
    board[row][col]=piece
    return board

#Gets a list of all the "lines" on the game board. Will work for square boards of side length = n
def getLines(board):
    lines =[]
    #Get Rows
    #The board has already got the rows nicely presented for us and it is trivial to add each row-line to our list of lines
    for row in board:
        lines.append(row)
    #Get Columns 
    #Not as easy but still trivial
    for col in range(0,width):
        newLine=[]
        for row in range(0,height):
            newLine.append(board[row][col])
        lines.append(newLine)

    #Get Diagonals
    #Harder to do programatically - will only work for square boards too
    #Downward Diagona has the same row and col index
    #Upward Diagonal has the row index backwards relative to the column 
    downwardDiag = []
    upwardDiag = []
    for row in range (0,height):
        downwardDiag.append(board[row][row])
        upwardDiag.append(board[height-1-row][row])
    lines.append(downwardDiag)
    lines.append(upwardDiag)
    return lines