#This is the file containing the methods associated with playing the game

import constant
whitespace = constant.EMPTY_SQUARE
height = constant.BOARD_HEIGHT
width=constant.BOARD_WIDTH
playerPiece = constant.PLAYER1_SYMBOL
computerPiece = constant.PLAYER2_SYMBOL

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

#helper function that checks if a square is empty. Returns a bool if so
def checkSquareEmpty(board,row,col):
    if (board[row][col]==whitespace):
        return True
    else:
        return False

#function to check if a specified player has won. This could be expanded for checking different combinations on nonsquare boards.
#Should currently be expandable to all square sized boards where the win condition is a full line.
def checkWin (board):
    #A player wins if they get a complete line. This means checking each column, each row, and both diagonals
    lines = []
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

    #Now that we have all the lines. 
    for line in lines:
        if ( (len(set(line)) == 1) & (line [0] != whitespace) ):
            return line[0]
        
    return None


#helper function that sets a square to the specified piece. Returns the new board 
def setBoardSquare(board,row,col,piece):
    board[row][col]=piece
    return board

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
        if (checkSquareEmpty(board,row,col)):
            processingMove=False
        else: 
            print ("The square was not empty")

    #Once we have the input we can put it on the board
    board = setBoardSquare(board,row,col,playerPiece)
    return (board)
        

#Initialise a game board and return it. 
def boardInit():
    board =  [[whitespace for x in range(width)] for y in range(height)]
    printBoard(board)
    return board