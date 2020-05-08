from tkinter import *
import numpy as np
import random
from tkinter import messagebox
root=Tk()
result=0
root.title("Tic Tac Toe ")
root.geometry("655x655")
board=np.zeros((3,3))
def initializeboard():     ###initialize all board values to 2 which represents blanks
    for i in range(0,3):
        for j in range(0,3):
            board[i][j]=2
initializeboard()
def boardvalues(i,j):         ###check board values before each turns
    return board[i][j]
def setboardvalues(i,j,value):
    board[i][j]=value     ### set board value "X" or "0"

def possiblewin(player):        ### 1st check winning possiblity of player 1(i.e at which blank he have to mark to win) and
    if player==2:                ### then check winning possiblity of player 2 (i.e at which blank he have to mark to block player 2 win)
        for i in range(0,3):
            if(board[i][0]*board[i][1]*board[i][2]==50):   ## check each row
                if(board[i][0]==2):
                    return i*3+1
                elif(board[i][1]==2):
                    return i*3+2
                else:
                    return i*3+3
        for i in range(0,3):                #check each column
            if (board[0][i]*board[1][i]*board[2][i]==50):
                if(board[0][i]==2):
                    return i+1
                elif(board[1][i]==2):
                    return i+4
                else:
                    return i+7
        if (board[0][0]*board[1][1]*board[2][2]==50): ## check 1st diagonal
            if(board[0][0]==2):
                return 1
            elif(board[1][1]==2):
                return 5
            else:
                return 9
        if (board[0][2]*board[1][1]*board[2][0]==50): ## check 2nd diagonal
            if(board[0][2]==2):
                return 3
            elif(board[1][1]==2):
                return 5
            else:
                return 7
        return 0
    else:
        for i in range(0,3):        ### then check winning possiblity of player 1 (i.e at which blank he have to mark to block player 1 win)
            if(board[i][0]*board[i][1]*board[i][2]==18):   ## check each row
                if(board[i][0]==2):
                    return i*3+1
                elif(board[i][1]==2):
                    return i*3+2
                else:
                    return i*3+3
        for i in range(0,3):                #check each column
            if (board[0][i]*board[1][i]*board[2][i]==18):
                if(board[0][i]==2):
                    return i+1
                elif(board[1][i]==2):
                    return i+4
                else:
                    return i+7
        if (board[0][0]*board[1][1]*board[2][2]==18): ## check 1st diagonal
            if(board[0][0]==2):
                return 1
            elif(board[1][1]==2):
                return 5
            else:
                return 9
        if (board[0][2]*board[1][1]*board[2][0]==18): ## check 2nd diagonal
            if(board[0][2]==2):
                return 3
            elif(board[1][1]==2):
                return 5
            else:
                return 7
        return 0

def checkwin(player):   ## check any player win or not
    if player==1:
        for i in range(0,3):
            if(board[i][0]*board[i][1]*board[i][2]==27):
                if i==0:
                    b1.config(bg="green")
                    b2.config(bg="green")
                    b3.config(bg="green")
                elif(i==1):
                    b4.config(bg="green")
                    b5.config(bg="green")
                    b6.config(bg="green")
                else:
                    b7.config(bg="green")
                    b8.config(bg="green")
                    b9.config(bg="green")

                return "true"
        for i in range(0,3):
            if(board[0][i]*board[1][i]*board[2][i]==27):
                if i==0:
                    b1.config(bg="green")
                    b4.config(bg="green")
                    b7.config(bg="green")
                elif(i==1):
                    b2.config(bg="green")
                    b5.config(bg="green")
                    b8.config(bg="green")
                else:
                    b3.config(bg="green")
                    b6.config(bg="green")
                    b9.config(bg="green")
                return "true"
        if(board[0][0]*board[1][1]*board[2][2]==27):
            b1.config(bg="green")
            b5.config(bg="green")
            b9.config(bg="green")
            return "true"
        if (board[0][2] * board[1][1] * board[2][0] == 27):
            b3.config(bg="green")
            b5.config(bg="green")
            b7.config(bg="green")
            return "true"
    if player==2:
        for i in range(0, 3):
            if (board[i][0] * board[i][1] * board[i][2] == 125):
                if i == 0:
                    b1.config(bg="green")
                    b2.config(bg="green")
                    b3.config(bg="green")
                elif (i == 1):
                    b4.config(bg="green")
                    b5.config(bg="green")
                    b6.config(bg="green")
                else:
                    b7.config(bg="green")
                    b8.config(bg="green")
                    b9.config(bg="green")

                return "true"
        for i in range(0, 3):
            if (board[0][i] * board[1][i] * board[2][i] == 125):
                if i == 0:
                    b1.config(bg="green")
                    b4.config(bg="green")
                    b7.config(bg="green")
                elif (i == 1):
                    b2.config(bg="green")
                    b5.config(bg="green")
                    b8.config(bg="green")
                else:
                    b3.config(bg="green")
                    b6.config(bg="green")
                    b9.config(bg="green")
                return "true"
        if (board[0][0] * board[1][1] * board[2][2] == 125):
            b1.config(bg="green")
            b5.config(bg="green")
            b9.config(bg="green")
            return "true"
        if (board[0][2] * board[1][1] * board[2][0] == 125):
            b3.config(bg="green")
            b5.config(bg="green")
            b7.config(bg="green")
            return "true"

def isboardfill():
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j]!=2:
                if i==2 and j==2:
                    return "true"
            else:
                return "false"
def randomblankbutton():
    count=0
    s=0
    for i in range(0,3):
        for j in range(0,3):
            if(board[i][j]==2):
                count=count+1
    print("count=",count)
    if count!=0:
        r=random.randint(1,count)
    else:
        r=0
    print("random number",r)
    for i in range(0,3):
        for j in range(0,3):
            if (board[i][j] == 2):
                s=s+1
            if s==r:
                if(i==0 and j==0):
                    return 1
                elif (i==0 and j==1):
                    return 2
                elif (i==0 and j==2):
                    return 3
                elif (i==1 and j==0):
                    return 4
                elif (i==1 and j==1):
                    return 5
                elif (i==1 and j==2):
                    return 6
                elif (i==2 and j==0):
                    return 7
                elif (i==2 and j==1):
                    return 8
                elif (i==2 and j==2):
                    return 9
def playcomputer():
    if possiblewin(2)!=0:
        movebutton=possiblewin(2)
        #print("Computer won better luck next time")
        #messagebox.showinfo("this is my popup","Computer won better luck next time")
        global result
        result="gameover"
        print(result)
    elif possiblewin(1)!=0:
        movebutton=possiblewin(1)
    else:
        movebutton=randomblankbutton()
        print("randombutton=",movebutton)
    if movebutton==1:
        b1.config(text="0")
        setboardvalues(0,0,5)
    elif movebutton==2:
        b2.config(text="0")
        setboardvalues(0,1,5)
    elif movebutton==3:
        b3.config(text="0")
        setboardvalues(0,2,5)
    elif movebutton==4:
        b4.config(text="0")
        setboardvalues(1,0,5)
    elif movebutton==5:
        b5.config(text="0")
        setboardvalues(1,1,5)
    elif movebutton==6:
        b6.config(text="0")
        setboardvalues(1,2,5)
    elif movebutton==7:
        b7.config(text="0")
        setboardvalues(2,0,5)
    elif movebutton==8:
        b8.config(text="0")
        setboardvalues(2,1,5)
    elif movebutton==9:
        b9.config(text="0")
        setboardvalues(2,2,5)
    if checkwin(2)=="true":
        result="gameover"
        print("game is over Computer won better luck next time")
        messagebox.showinfo("this is my popup", "Computer won better luck next time")


def func1():
    global result
    if result==0:
        if board[0,0]!=3 and board[0][0]!=5:
            setboardvalues(0,0,3)
            print("isboardfill ",isboardfill())
            b1.config(text="X")
            if(checkwin(1)=="true"):
                print("You Won Congrats")
                messagebox.showinfo("this is my popup", "you won congrats")
                result="gameover"
                print(result)
            elif(isboardfill()=="true"):
                print("game is draw")
                messagebox.showinfo("this is my popup", "game is draw")
                initializeboard()
            else:
                playcomputer()
                print(board)
        else:
            print("you cant click here again")
            messagebox.showwarning("this is my popup", "you cant click here")


    else:
        messagebox.showinfo("this is my popup", "GameOver")
        print("gameover")
def func2():
    global result
    if result == 0:
        if board[0, 1] != 3 and board[0][1] != 5:
            setboardvalues(0,1,3)
            print("isboardfill ", isboardfill())
            b2.config(text="X")
            if(checkwin(1)=="true"):
                result = "gameover"
                print(result)
                print("You Won Congrats")
                messagebox.showinfo("this is my popup", "you won congrats")
                #initializeboard()
            elif(isboardfill()=="true"):
                print("game is draw")
                messagebox.showinfo("this is my popup", "game is draw")
                initializeboard()
            else:
                playcomputer()
                print(board)
        else:
            print("you cant click here again")
            messagebox.showwarning("this is my popup", "you won congrats")
    else:
        messagebox.showinfo("this is my popup", "gameover")
        print("gameover")
def func3():
    global result
    if result == 0:
        if board[0, 2] != 3 and board[0][2] != 5:
            setboardvalues(0,2,3)
            print("isboardfill ", isboardfill())
            b3.config(text="X")
            if(checkwin(1)=="true"):
                result = "gameover"
                print(result)
                print("You Won Congrats")
                messagebox.showinfo("this is my popup", "you won congrats")
                #initializeboard()
            elif(isboardfill()=="true"):
                print("game is draw")
                messagebox.showinfo("this is my popup", "game is draw")
                initializeboard()
            else:
                playcomputer()
                print(board)
        else:
            print("you cant click here again")
            messagebox.showinfo("this is my popup", "you cant click here again")
    else:
        messagebox.showinfo("this is my popup", "gameover")
        print("game over")
def func4():
    global result
    if result==0:
        if board[1, 0] != 3 and board[1][0] != 5:
            setboardvalues(1,0,3)
            print("isboardfill ", isboardfill())
            b4.config(text="X")
            if(checkwin(1)=="true"):
                messagebox.showinfo("this is my popup", "You won congrats")
                print("You Won Congrats")
                result = "gameover"
                print(result)
                #initializeboard()
            elif(isboardfill()=="true"):
                print("game is draw")
                messagebox.showinfo("this is my popup", "game is draw")
                initializeboard()
            else:
                playcomputer()
                print(board)
        else:
            print("you cant click here again")
            messagebox.showwarning("this is my popup", "you cant click here again")
    else:
        print("gameover")
        messagebox.showinfo("this is my popup", "gameover")
def func5():
    global result
    if result==0:
        if board[1, 1] != 3 and board[1][1] != 5:
            setboardvalues(1,1,3)
            print("isboardfill ", isboardfill())
            b5.config(text="X")
            if(checkwin(1)=="true"):
                print("You Won Congrats")
                messagebox.showinfo("this is my popup", "you won congrats")
                result = "gameover"
                #initializeboard()
            elif(isboardfill()=="true"):
                print("game is draw")
                messagebox.showinfo("this is my popup", "game is draw")
                initializeboard()
            else:
                playcomputer()
                print(board)
        else:
            print("you cant click here again")
            messagebox.showwarning("this is my popup", "you cant click here again")
    else:
        print("gameover")
        messagebox.showinfo("this is my popup", "gameover")
def func6():
    global result
    if result==0:
        if board[1, 2] != 3 and board[1][2] != 5:
            setboardvalues(1,2,3)
            print("isboardfill ", isboardfill())
            b6.config(text="X")
            if(checkwin(1)=="true"):
                print("You Won Congrats")
                messagebox.showinfo("this is my popup", "you won congrats")
                result = "gameover"
                #initializeboard()
            elif(isboardfill()=="true"):
                print("game is draw")
                messagebox.showinfo("this is my popup", "game is draw")
                initializeboard()
            else:
                playcomputer()
                print(board)
        else:
            print("you cant click here again")
            messagebox.showinfo("this is my popup", "you cant click here again")
    else:
        print("gameover")
        messagebox.showinfo("this is my popup", "gameover")
def func7():
    global result
    if result==0:
        if board[2, 0] != 3 and board[2][0] != 5:
            setboardvalues(2,0,3)
            print("isboardfill ", isboardfill())
            b7.config(text="X")
            if(checkwin(1)=="true"):
                print("You Won Congrats")
                messagebox.showinfo("this is my popup", "you won congrats")
                result = "gameover"
                #initializeboard()
            elif(isboardfill()=="true"):
                print("game is draw")
                messagebox.showinfo("this is my popup", "game over")
                initializeboard()
            else:
                playcomputer()
                print(board)
        else:
            print("you cant click here again")
            messagebox.showwarning("this is my popup", "you cant click here again")
    else:
        print("gameover")
        messagebox.showinfo("this is my popup", "gameover")
def func8():
    global result
    if result==0:
        if board[2, 1] != 3 and board[2][1] != 5:
            setboardvalues(2,1,3)
            print("isboardfill ", isboardfill())
            b8.config(text="X")
            if(checkwin(1)=="true"):
                print("You Won Congrats")
                messagebox.showinfo("this is my popup", "you won congrats")
                result = "gameover"
                #initializeboard()
            elif(isboardfill()=="true"):
                print("game is draw")
                messagebox.showinfo("this is my popup", "game is draw")
                initializeboard()
            else:
                playcomputer()
                print(board)
        else:
            print("you cant click here again")
            messagebox.showwarning("this is my popup", "you cant click here")
    else:
        print("gameover")
        messagebox.showinfo("this is my popup", "gameover")
def func9():
    global result
    if result==0:
        if board[2, 2] != 3 and board[2][2] != 5:
            setboardvalues(2,2,3)
            print("isboardfill ", isboardfill())
            b9.config(text="X")
            if(checkwin(1)=="true"):
                print("You Won Congrats")
                messagebox.showinfo("this is my popup", "you won congrats")
                result = "gameover"
                #initializeboard()
            elif(isboardfill()=="true"):
                print("game is draw")
                messagebox.showinfo("this is my popup", "game is draw")
                initializeboard()
            else:
                playcomputer()
                print(board)
        else:
            print("you cant click here again")
            messagebox.showwarning("this is my popup", "you cant click here again")
    else:
        print("gameover")
        messagebox.showinfo("this is my popup", "gameover")



b1=Button(text="",height=10,width=20,command=func1)
b1.grid(row=0,column=0,padx=5,pady=5)

b2=Button(text="",height=10,width=20, command=func2)
b2.grid(row=0,column=1,padx=5,pady=5)

b3=Button(text="",height=10,width=20, command=func3)
b3.grid(row=0,column=2,padx=5,pady=5)

b4=Button(text="",height=10,width=20, command=func4)
b4.grid(row=1,column=0,padx=5,pady=5)

b5=Button(text="",height=10,width=20, command=func5)
b5.grid(row=1,column=1,padx=5,pady=5)

b6=Button(text="",height=10,width=20, command=func6)
b6.grid(row=1,column=2,padx=5,pady=5)

b7=Button(text="",height=10,width=20, command=func7)
b7.grid(row=2,column=0,padx=5,pady=5)

b8=Button(text="",height=10,width=20, command=func8)
b8.grid(row=2,column=1,padx=5,pady=5)

b9=Button(text="",height=10,width=20, command=func9)
b9.grid(row=2,column=2,padx=5,pady=5)

label=Label(root,text="player 1 is you which plays X")
label.place(x=490,y=1)

label=Label(root,text="player 2 is computer which plays 0")
label.place(x=490,y=50)

root.mainloop()
