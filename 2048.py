
#2048 game
import random
from tkinter import *

root=Tk()

score = 0
highscore = 0
colors={
    0:"white",
    2:"lavenderblush",
    4:"bisque",
    8:"tan",
    16:"gray",
    32:"lightblue",
    64:"forestgreen",
    128:"gold",
    256:"pink",
    512:"orange",
    1024:"yellow",
    2048:"red"
    }

board = []
squares = []
def newgame():
    global board
    #fill board
    board = []
    row = []
    for i in range(4):
        row.append(0)
    for j in range(4):
        board.append(row.copy())
    newnumber()
    newnumber()
    newnumber()
    newnumber()




def makeboard():
    global squares
    title = Label(root, text="2048 Game", font="Arial 17 bold")
    title.grid(row=0, column=0, columnspan=4)
    instruc = Label(root, text= "Use arrow keys to move", font="Arial 12")
    instruc.grid(row=1, column=0, columnspan=4)
    restart = Button(root, text="New Game", font = "Arial 12 bold")
    restart.grid(row=6, column=0, columnspan=2)
    quitBtn = Button(root, text="Quit", font = "Arial 14 bold")
    quitBtn.grid(row=6, column=2, columnspan=2)
    for r in range(4):
        temprow = []
        for c in range(4):
            templabel = Label(root, height=2, width=4, relief="ridge", font="Arial 16 bold")
            temprow.append(templabel)
        squares.append(temprow)
    for r in range(4):
        for c in range(4):
            sq = squares[r][c]
            sq.grid(row=r+2, column=c)

        
def showboard():
    for j in range(4):
        row = ""
        for i in range(4):
            row = row + str(board[i][j]) + " "
        print(row)


def displayboard():
    global squares
    for r in range(4):
        for c in range(4):
            mycolor=colors[board[r][c]]
            squares[r][c].config(text=board[r][c], bg = mycolor)
            
            
def newnumber():
    newnum = 0
    newrow = random.randint(0,3)
    newcol = random.randint(0,3)
    while board[newrow][newcol] != 0:
        newrow = random.randint(0,3)
        newcol = random.randint(0,3)
    rand = random.randint(1,100)
    if rand < 80:
        newnum = 16
    else:
        newnum = 4
    board[newrow][newcol] = newnum

def moveleft(e):
        rotate(2)
        swiperight()
        rotate(2)
        displayboard()
def moveright(e):
        swiperight()
        displayboard()
def moveup(e):
        rotate(3)
        swiperight()
        rotate(1)
        displayboard()
def movedown(e):
        rotate(1)
        swiperight()
        rotate(3)
        displayboard()
def bindkeys():
    global root
    root.bind("<Down>", movedown)
    root.bind("<Up>", moveup)
    root.bind("<Right>", moveright)
    root.bind("<Left>", moveleft)
def swiperight():
    global board
    #a function to add the numbers and move them right
    for row in board:
        
        for i in range(3):
            n1 = row[i]
            n2 = row[i+1]
            if n1 == n2 or n2 == 0:
                row[i] = 0
                row[i+1] = n1 + n2
                
        for i in range(2):
            n1 = row[i]
            n2 = row[i+1]
            if n1 == n2 or n2 == 0:
                row[i] = 0
                row[i+1] = n1 + n2
def rotate(number_turns):
    global board
    # a function to rotate the board some number of quarter turns clockwise
    for j in range(number_turns):
        temp1 = []
        temp2 = []
        temp3 = []
        temp4 = []
        for i in range (3,-1,-1):
            temp1.append(board[i][0])
            temp2.append(board[i][1])
            temp3.append(board[i][2])
            temp4.append(board[i][3])
        board = []
        board.append(temp1)
        board.append(temp2)
        board.append(temp3)
        board.append(temp4)
def checkwin():
    win = False
    for row in board:
        for item in row:
            if item ==2048:
                win=True
    return win

makeboard()
newgame()
displayboard()
bindkeys()

root.mainloop()
