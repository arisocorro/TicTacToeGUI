import tkinter as tk
from tkinter.constants import DISABLED, NORMAL
from tkinter import messagebox
from tkinter import Canvas
import random

# --- COLORS CONSTANTS -----
BACKGROUND = '#2b3e4f'
WHITE      = '#fefefa'
BLUE       = '#4c9aeb'
LIGHT_BLUE = '#5bbfdd'
GREEN      = '#5bb75f'
RED        = '#d9544d'
YELLOW     = '#eeae4c'
BLACK      = '#191919'
PURPLE     = '#9632c7'

# -------------------------------------------------------
# Game Start Screen
# -------------------------------------------------------

class Grid:

    def __init__(self):
        self.root = tk.Tk()
        self.root.config(bg=BACKGROUND)
        self.root.geometry("300x235")
        self.root.title("Tic-Tac-Toe Player Select")

        # Label title
        self.startBanner = tk.Label(self.root, text="--- Welcome to Tic-Tac-Toe! ---", font=('Niagara Solid', 20, 'underline'), bg=BACKGROUND , fg=WHITE)
        self.startBanner.config(anchor='center')
        self.startBanner.pack(pady=10)

        # Label Player Select
        self.playerSelect = tk.Label(self.root, text="Select your Character: ", font=('Niagara Solid', 15), bg=BACKGROUND, fg=WHITE)
        self.playerSelect.pack(padx=10,pady=10)

        self.buttonFrame = tk.Frame(self.root)

        self.buttonFrame.columnconfigure(0, weight=1)
        self.buttonFrame.columnconfigure(1, weight=1)

        self.buttonFrame.config(bg=BACKGROUND)

        # Player selection buttons
        self.xButton = tk.Button(self.buttonFrame, text="X", font=('Niagara Solid', 15), command=self.xSelect, state=NORMAL, bg=LIGHT_BLUE, fg=WHITE)
        self.xButton.grid(row=0, column=0, sticky=tk.W + tk.E, padx=5)

        self.oButton = tk.Button(self.buttonFrame, text="O", font=('Niagara Solid', 15), command=self.oSelect, state=NORMAL, bg=LIGHT_BLUE, fg=WHITE)
        self.oButton.grid(row=0, column=1, sticky=tk.W + tk.E, padx=5)

        self.buttonFrame.pack(fill='x')
        self.root.mainloop()

    # Player Select - outputs selected playerChar and gives option to Quit or Start game
    def xSelect(self):
        global playerChar
        global oppChar
        playerChar = 'X'
        oppChar = 'O'
        self.playerLabel = tk.Label(self.root,  text='You have selected '+playerChar,
                                    font=('Niagara Solid', 15), bg=BACKGROUND, fg=WHITE).pack(pady=10)
        self.xButton.config(state=DISABLED)
        self.oButton.config(state=DISABLED)
        self.startQuit()

    def oSelect(self):
        global playerChar
        global oppChar
        playerChar = 'O'
        oppChar = 'X'
        self.playerLabel =tk.Label(self.root, text='You have selected '+playerChar,
                                   font=('Niagara Solid', 15), bg=BACKGROUND, fg=WHITE).pack(pady=10)
        self.xButton.config(state=DISABLED)
        self.oButton.config(state=DISABLED)
        self.startQuit()

    def startQuit(self):
        self.startQuitButtonFrame = tk.Frame(self.root)

        self.startQuitButtonFrame.config(bg='#2b3e4f')

        self.startQuitButtonFrame.columnconfigure(0, weight=1)
        self.startQuitButtonFrame.columnconfigure(1, weight=1)

        self.startButton = tk.Button(self.startQuitButtonFrame, text="Start!", font=('Niagara Solid', 15),command=self.DifficultyScreen,bg=GREEN, fg=WHITE)
        self.startButton.grid(row=0,column=0,sticky=tk.W + tk.E, padx=5)

        self.quitButton = tk.Button(self.startQuitButtonFrame, text="Quit!", font=('Niagara Solid', 15), command=self.destroy, bg=RED, fg=WHITE)
        self.quitButton.grid(row=0, column=1, sticky=tk.W + tk.E, padx=5)

        self.startQuitButtonFrame.pack(fill='x')

    def destroy(self):
        self.root.destroy()

    def DifficultyScreen(self):
        self.root.destroy()
        DifficultySelect()

# -------------------------------------------------------
# Difficulty Selection Screen
# -------------------------------------------------------

class DifficultySelect:
    def __init__(self):
        self.rootDif = tk.Tk()
        self.rootDif.config(bg=BACKGROUND)
        self.rootDif.geometry("300x140")
        self.rootDif.title("Select Dificulty")

        self.selectionLabel = tk.Label(self.rootDif, text="--- Select Opponent ---", font=('Niagara Solid', 20, 'underline'), bg=BACKGROUND, fg=WHITE)
        self.selectionLabel.config(anchor='center')
        self.selectionLabel.pack(pady=10)


        self.selectionFrame = tk.Frame(self.rootDif)
        self.selectionFrame.config(bg=BACKGROUND)

        self.selectionFrame.columnconfigure(0, weight=1)
        self.selectionFrame.columnconfigure(1, weight=1)

        self.randomSelect = tk.Button(self.selectionFrame,text="Random", font=('Niagara Solid', 15), command = self.gameStartRandom, bg=BLUE, fg=WHITE)
        self.randomSelect.grid(row=0, column=0, sticky=tk.W + tk.E, padx=5)

        self.minmaxSelect = tk.Button(self.selectionFrame,text="MinMax", font=('Niagara Solid', 15), command = self.gameStartMinMax, bg=YELLOW, fg=WHITE)
        self.minmaxSelect.grid(row=0, column=1, sticky=tk.W + tk.E, padx=5)

        self.selectionFrame.pack(fill='x')

        self.backButton = tk.Button(self.rootDif, text="Back", width= 10 ,font=('Niagara Solid', 15), command = self.back,bg=RED, fg=WHITE)
        self.backButton.pack(pady=10)

        self.rootDif.mainloop()

    def gameStartRandom(self):
        global minmax
        minmax = False
        print(f"This is minmax value: {minmax}")
        self.rootDif.destroy()
        GameBoard()

    def gameStartMinMax(self):
        global minmax
        minmax = True
        print(f"This is minmax value: {minmax}")
        self.rootDif.destroy()
        GameBoard()

    def back(self):
        self.rootDif.destroy()
        Grid()

# -------------------------------------------------------
# Start Of Tic Tac Toe Game
# -------------------------------------------------------

class GameBoard:
    def __init__(self):
        self.isTurn = False
        self.window = tk.Tk()
        if minmax:
            self.window.title("Tic-Tac-Toe ---- MinMax")
        else:
            self.window.title("Tic-Tac-Toe ---- Random")

        self.buttons = [[0,0,0],
                        [0,0,0],
                        [0,0,0]]

        self.buttonFrame = tk.Frame(self.window)

        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(self.buttonFrame, text="", font=('Niagara Solid', 50), height=1, width= 5,
                                              command= lambda row=row, column=col: self.place(row,column),bd=3, bg=BACKGROUND, fg=BLACK)
                self.buttons[row][col].grid(row=row,column=col)

        self.buttonFrame.pack()

        self.window.mainloop()

    # Attempts to place piece and
    def place(self,row, col):
        if self.buttons[row][col]['text'] == "" and self.checkWinner() is False:
            self.buttons[row][col]['text'] = playerChar
            self.buttons[row][col]['fg'] = GREEN
            self.isTurn = True
        elif self.buttons[row][col]['text'] != "" and self.checkWinner() is False:
            messagebox.showerror(title="Placement Error", message="Someone has already claimed that spot \nPlease choose another...")


        # -------------------------------------------------------
        # Game End - Player Win
        # -------------------------------------------------------

        if self.checkWinner():
            self.outputWinner()
            if messagebox.askyesno(title="You Win... Somehow... ",message="Would you like you play again?" ):
                self.window.destroy()
                DifficultySelect()
            else:
                self.window.destroy()

        #Random or MinMax Comp AI
        if self.isTurn:
            if minmax:
                self.opp_MinMax()
                self.isTurn = False
            else:
                self.opp_random()
                self.isTurn = False

    def checkWinner(self):
        # check rows
        for row in range(3):
            if self.buttons[row][0]['text'] == self.buttons[row][1]['text'] == self.buttons[row][2]['text'] != "": return True
        # check cols
        for col in range(3):
            if self.buttons[0][col]['text'] == self.buttons[1][col]['text'] == self.buttons[2][col]['text'] != "": return True

        # check diagonals
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "": return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "": return True

        # -------------------------------------------------------
        # Game End - Tie
        # -------------------------------------------------------

        if self.NoSpaces():
            if messagebox.askyesno(title="It's a Tie! ",message="Would you like you play again?" ):
                self.window.destroy()
                DifficultySelect()

            else:
                self.window.destroy()

        return False

    # Check if there are spaces left on board
    def NoSpaces(self):
        for row in range(3):
            for col in range(3):
                if self.buttons[row][col]['text'] == "": return False

        return True

    # -------------------------------------------------------
    # Random Ai
    # -------------------------------------------------------
    def opp_random(self):
        if self.NoSpaces():
            if messagebox.askyesno(title="It's a Tie! ", message="Would you like you play again?"):
                self.window.destroy()
                DifficultySelect()

            else:
                self.window.destroy()

        options = self.emptySpaces()
        row, col = random.choice(options)
        if self.buttons[row][col]['text'] == "" and self.checkWinner() is False:
            self.buttons[row][col]['text'] = oppChar
            self.buttons[row][col]['fg'] = BLUE

        if self.checkWinner():
            self.outputWinner()
            if messagebox.askyesno(title="You Lose!",message="Unlucky Rubber Ducky \nWould you like you play again?" ):
                self.window.destroy()
                DifficultySelect()

            else:
                self.window.destroy()

    # -------------------------------------------------------
    # Minmax Ai
    # -------------------------------------------------------
    def opp_MinMax(self):
        bestScore = -100
        bestMove = 0,0
        board = self.boardState()

        for i,char in enumerate(board):
            if char == '0':
                board[i] = oppChar
                score = self.minmax(board,False)
                board[i] = '0'
                if score > bestScore:
                    bestScore = score
                    bestMove = self.bestMoveConverstion(i)

        self.insertOppVal(bestMove)

    def minmax(self, board, isMaximizing):
        if self.checkWhoWin(oppChar, board):return 1
        if self.checkWhoWin(playerChar,board): return -1
        if self.checkDraw(board):return 0

        if isMaximizing:
            bestScore = -100
            for i, char in enumerate(board):
                if char == '0':
                    board[i] = oppChar
                    score = self.minmax(board, False)
                    board[i] = '0'
                    if score > bestScore:
                        bestScore = score
            return bestScore
        else:
            bestScore = 100
            for i, char in enumerate(board):
                if char == '0':
                    board[i] = playerChar
                    score = self.minmax(board, True)
                    board[i] = '0'
                    if score < bestScore:
                        bestScore = score
            return bestScore

    def checkWhoWin(self, player,board):
        winCon = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for i in range(0,8):
            if (board[winCon[i][0]] == player and board[winCon[i][1]] == player and board[winCon[i][2]] == player):
                return True
        return False

    def checkDraw(self,board):
        for i in range(0,8):
            if board[i] == '0':
                return False
        return True

    def bestMoveConverstion(self, move):
        row = int(move /3)
        col = int(move %3)
        return row,col

    def insertOppVal(self,insertVal):
        row = insertVal[0]
        col = insertVal[1]

        if self.buttons[row][col]['text'] == "" and self.checkWinner() is False:
            self.buttons[row][col]['text'] = oppChar
            self.buttons[row][col]['fg'] = YELLOW

        if self.checkWinner():
            self.outputWinner()
            if messagebox.askyesno(title="You Lose!",message="Unlucky Rubber Ducky \nWould you like you play again?" ):
                self.window.destroy()
                DifficultySelect()

            else:
                self.window.destroy()

    def emptySpaces(self):
        empty = []
        for row in range(3):
            for col in range(3):
                if self.buttons[row][col]['text'] == "":
                    empty.append([row,col])
        return empty

    def boardState(self):
        board = ['0','0','0','0','0','0','0','0','0']
        count = 0
        for row in range(3):
            for col in range(3):
                if self.buttons[row][col]['text'] == playerChar:
                    board[count] = playerChar
                if self.buttons[row][col]['text'] == oppChar:
                    board[count] = oppChar
                count += 1
        return board

    # -------------------------------------------------------
    # Winner Output --- Visual
    # -------------------------------------------------------

    def outputWinner(self):
        # Get the state of the board
        board = self.boardState()
        # Determine positions of the winner
        pos1,pos2,pos3 = self.winnerPos(board)
        # Draw canvas to depict winner
        self.winnerButton(pos1)
        self.winnerButton(pos2)
        self.winnerButton(pos3)

    def winnerPos(self,board):
        winCon = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for i in range(0, 8):
            if (board[winCon[i][0]] == board[winCon[i][1]] == board[winCon[i][2]] != ''):
                return winCon[i][0],winCon[i][1],winCon[i][2]

    def winnerButton(self, pos):
        row,col = self.bestMoveConverstion(pos)
        self.buttons[row][col]['bg'] = LIGHT_BLUE

if __name__ == "__main__":
    Grid()


