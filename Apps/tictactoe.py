import tkinter
from cmath import inf
import time

turn = 'X'
alpha = 12435
beta = 324356
opponent = 0
vacancy = 1

def adraworwhat(board):
    for i in range(3):
        for j in range(3):
            if (board[i][j] == 'X' or board[i][j] == 'O') == 0:
                return 0
    return 1

def iwonorwhat(letter,board):
    a = ((board[0][0] == letter)and(board[0][1] == letter)and(board[0][2] == letter))or((board[1][0] == letter)and(board[1][1] == letter)and(board[1][2] == letter))or((board[2][0] == letter)and(board[2][1] == letter)and(board[2][2] == letter))or((board[0][0] == letter)and(board[1][0] == letter)and(board[2][0] == letter))or((board[0][1] == letter)and(board[1][1] == letter)and(board[2][1] == letter))or((board[0][2] == letter)and(board[1][2] == letter)and(board[2][2] == letter))or((board[0][0] == letter)and(board[1][1] == letter)and(board[2][2] == letter))or((board[0][2] == letter)and(board[1][1] == letter)and(board[2][0] == letter))
    return a

def find_moves(game_board):
    moves = []
    for i in range(3):
        for j in range(3):
            if (game_board[i][j] == 'X' or game_board[i][j] == 'O') == 0:
                lis = [i,j]
                moves.append(lis)
    return moves

def make_move(game_board , i , j , letter):
    new_game_board = [[game_board[b][a] for a in range(3)] for b in range(3)]
    new_game_board[i][j] = letter
    return new_game_board



def return_eval(game_board , letter,depth):
    global alpha,beta
    depth += 1

    if iwonorwhat('X' , game_board):
        return float('inf')
    if iwonorwhat('O',game_board):
        return float('-inf')
    if adraworwhat(game_board):
        return 0

    if letter == 'X':
        eval = float('-inf')
        i_like_to_move_it_move_it = find_moves(game_board)
        for i in i_like_to_move_it_move_it:
            new_game_board = make_move(game_board , i[0] , i[1] , 'X')
            move_value = return_eval(new_game_board , 'O',depth)
            if move_value >= eval:
                if depth == 1:
                    alpha = i[0]
                    beta = i[1]
                eval = move_value

        return eval
    if letter == 'O':
        eval = float('inf')
        i_like_to_move_it_move_it = find_moves(game_board)
        for i in i_like_to_move_it_move_it:
            new_game_board = make_move(game_board , i[0] , i[1] , 'O')
            move_value = return_eval(new_game_board , 'X',depth)
            if move_value <= eval:
                if depth == 1:
                    alpha = i[0]
                    beta = i[1]
                eval = move_value

        return eval

def gamescreen():
    window = tkinter.Tk()
    window.title("game")
    window.geometry('300x300')

    board = [[0 for a in range(3)] for b in range(3)]
    frame = tkinter.Frame(window , highlightthickness=4 , highlightbackground= "blue")
    frame.pack(padx=20,pady=40)

    for i in range(3):
        for j in range(3):
            huh = tkinter.Button(frame,font = ("Comic Sans MS",8),command=lambda a=i, b=j:clicked(a,b,board,window,frame),height = 2 , width = 4)
            huh.grid(column=i,row=j)
            board[i][j] = huh
            
    return [window,board,frame]

def new_game(mode):
    global opponent,turn,vacancy
    vacancy = 1
    if mode == 0:
        huh = gamescreen()
        opponent = 0
        turn = 'X'
        
    elif mode == 1:
        huh = gamescreen()
        opponent = 1
        turn = 'X'
        
    elif mode == 2:
        huh = gamescreen()
        opponent = 1
        huh[1][0][0]['text'] = 'X'
        huh[1][0][0].config(fg = "blue")
        huh[2].config(highlightbackground = "green")
        turn = 'O'

def pc_new_game():
    hey = tkinter.Tk()
    hey.title("")
    hey.geometry('300x300')
    newgame = tkinter.Button(hey , text = "Play as X",font = ("Comic Sans MS",10), fg = "blue" , command = lambda : new_game(1))
    newgame.pack()
    pc_newgame = tkinter.Button(hey , text = "Play as O",font = ("Comic Sans MS",10), fg = "green",command = lambda : new_game(2))
    pc_newgame.pack()
    leavegame = tkinter.Button(hey , text = "Back to menu",font = ("Comic Sans MS",10),fg = "red",command=lambda:leave_pc(hey))
    leavegame.pack()
    hey.mainloop()

def leave_pc(hey):
    hey.destroy()

def didiwinquestionmark(letter,board):
    wheredidiwin = [[]]
    didiwin = 0
    if ((board[0][0].cget('text') == letter)and(board[0][1].cget('text') == letter)and(board[0][2].cget('text') == letter)):
        wheredidiwin.append([0,0])
        wheredidiwin.append([0,1])
        wheredidiwin.append([0,2])
        didiwin = 1
    if ((board[1][0].cget('text') == letter)and(board[1][1].cget('text') == letter)and(board[1][2].cget('text') == letter)):
        wheredidiwin.append([1,0])
        wheredidiwin.append([1,1])
        wheredidiwin.append([1,2])
        didiwin = 1
    if ((board[2][0].cget('text') == letter)and(board[2][1].cget('text') == letter)and(board[2][2].cget('text') == letter)):
        wheredidiwin.append([2,0])
        wheredidiwin.append([2,1])
        wheredidiwin.append([2,2])
        didiwin = 1
    if ((board[0][0].cget('text') == letter)and(board[1][0].cget('text') == letter)and(board[2][0].cget('text') == letter)):
        wheredidiwin.append([0,0])
        wheredidiwin.append([1,0])
        wheredidiwin.append([2,0])
        didiwin = 1
    if ((board[0][1].cget('text') == letter)and(board[1][1].cget('text') == letter)and(board[2][1].cget('text') == letter)):
        wheredidiwin.append([0,1])
        wheredidiwin.append([1,1])
        wheredidiwin.append([2,1])
        didiwin = 1
    if ((board[0][2].cget('text') == letter)and(board[1][2].cget('text') == letter)and(board[2][2].cget('text') == letter)):
        wheredidiwin.append([0,2])
        wheredidiwin.append([1,2])
        wheredidiwin.append([2,2])
        didiwin = 1
    if ((board[0][0].cget('text') == letter)and(board[1][1].cget('text') == letter)and(board[2][2].cget('text') == letter)):
        wheredidiwin.append([0,0])
        wheredidiwin.append([1,1])
        wheredidiwin.append([2,2])
        didiwin = 1
    if ((board[0][2].cget('text') == letter)and(board[1][1].cget('text') == letter)and(board[2][0].cget('text') == letter)):
        wheredidiwin.append([0,2])
        wheredidiwin.append([1,1])
        wheredidiwin.append([2,0])
        didiwin = 1

    return [didiwin , wheredidiwin]

def isthisadrawquestionmark(board):
    for i in range(3):
        for j in range(3):
            if (board[i][j].cget('text') == 'X' or board[i][j].cget('text') == 'O') == 0:
                return 0
    return 1

def winanimation(board,winline,frame):
    for fir in range(3):
        for sec in range(3):
            if [fir,sec] not in winline:
                if board[fir][sec]['text'] == 'X':
                    board[fir][sec].config(fg = "light blue")
                if board[fir][sec]['text'] == 'O':
                    board[fir][sec].config(fg = "light green")
                board[fir][sec].update()
                time.sleep(0.2)
                board[fir][sec]['text'] = ''
                board[fir][sec].update()
            else:
                board[fir][sec].config(fg = "black")
                board[fir][sec].update()
                time.sleep(0.2)
    frame.config(highlightbackground = "red")
    frame.update()
    time.sleep(0.2)

                
def drawanimation(board,frame):
    for fir in range(3):
        for sec in range(3):
            board[fir][sec].config(fg = "black")
            board[fir][sec].update()
            time.sleep(0.2)
    frame.config(highlightbackground = "red")
    frame.update()
    time.sleep(0.2)
    

def clicked(i,j,board,window,frame):
    global turn,opponent,alpha,beta,vacancy
    if vacancy == 0:
        return
    vacancy = 0
    if (board[i][j].cget('text') == 'X' or board[i][j].cget('text') == 'O') == 0:
        if turn == 'X':   
            board[i][j]['text'] = 'X'
            board[i][j].config(fg = "blue")
            frame.config(highlightbackground = "green")
        if turn == 'O':   
            board[i][j]['text'] = 'O'
            board[i][j].config(fg = "green")
            frame.config(highlightbackground = "blue")
        board[i][j].update()
        results = didiwinquestionmark(turn,board)
        if results[0] == 1:
            winanimation(board , results[1],frame)   
            if turn == 'X':
                message = "X wins!"
                ll = tkinter.Label(window , text=message , fg = "black" ,font = ("Comic Sans MS",20))
            elif turn == 'O':
                message = "O wins!"
                ll = tkinter.Label(window , text=message , fg = "black" , font = ("Comic Sans MS",20))
            ll.pack()
            ll.update()
            time.sleep(2.5)
            window.destroy()
        if isthisadrawquestionmark(board) == 1:
            drawanimation(board,frame)
            message = "It's a Draw!"
            ll = tkinter.Label(window , text=message , fg = "black" ,font = ("Comic Sans MS",20))
            ll.pack()
            ll.update()
            frame.update()
            time.sleep(2.5)
            window.destroy()
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        if opponent:
            time.sleep(0.25)
            gameboard = [[board[a][b].cget('text') for a in range(3)] for b in range(3)]
            return_eval(gameboard , turn , 0)
            if turn == 'X':   
                board[beta][alpha]['text'] = 'X'
                board[beta][alpha].config(fg = "blue")
                frame.config(highlightbackground = "green")
            if turn == 'O':   
                board[beta][alpha]['text'] = 'O'
                board[beta][alpha].config(fg = "green")
                frame.config(highlightbackground = "blue")
            board[beta][alpha].update()

            results = didiwinquestionmark(turn,board)
            if results[0] == 1:
                winanimation(board , results[1],frame)   
                if turn == 'X':
                    message = "X wins!"
                    ll = tkinter.Label(window , text=message , fg = "black" ,font = ("Comic Sans MS",20))
                elif turn == 'O':
                    message = "O wins!"
                    ll = tkinter.Label(window , text=message , fg = "black" , font = ("Comic Sans MS",20))
                ll.pack()
                ll.update()
                time.sleep(2.5)
                window.destroy()
            if isthisadrawquestionmark(board) == 1:
                drawanimation(board,frame)
                message = "It's a Draw!"
                ll = tkinter.Label(window , text=message , fg = "black" ,font = ("Comic Sans MS",20))
                ll.pack()
                ll.update()
                frame.update()
                time.sleep(2.5)
                window.destroy()
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
    vacancy = 1
        
def leave_game():
    woah.destroy()

woah = tkinter.Tk()
woah.title("menu")
woah.geometry('300x300')
pc_newgame = tkinter.Button(woah , text = "Play against computer",font = ("Comic Sans MS",10), fg = "blue" ,command = lambda : pc_new_game())
pc_newgame.pack()
newgame = tkinter.Button(woah , text = "Play against friend",font = ("Comic Sans MS",10), fg = "green",command = lambda : new_game(0))
newgame.pack()
leavegame = tkinter.Button(woah , text = "Exit",font = ("Comic Sans MS",10), fg = "red",command=lambda:leave_game())
leavegame.pack()

woah.mainloop()

#ff0000   red
#00cc00   green
# 0000e6 or 0000cc blue nice