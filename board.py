from tkinter import *
from tkinter import messagebox

class Board:
    def __init__(self):
        self.board = [['', '', ''],
                      ['', '', ''],
                      ['', '', '']]
        self.root = Tk()
        self.root.title('Tic-Tac-Toe')
        self.canvas = Canvas(self.root, width=500, height=500, bg='gray')
        self.canvas.grid()

    def draw_board(self):
        # Create vertical lines
        self.canvas.create_line(180, 50, 180, 410, width=3)
        self.canvas.create_line(310, 50, 310, 410, width=3)
        # Create horizontal lines
        self.canvas.create_line(50, 170, 440, 170, width=3)
        self.canvas.create_line(50, 290, 440, 290, width=3)

    def run(self):
        self.root.mainloop()

    def new_game(self):
        again = messagebox.askquestion(title='New Game', message="Would you like to play a new game?")

    def clear_board(self):
        for row in self.board:
            for i in range(len(row)):
                row[i] = ''
