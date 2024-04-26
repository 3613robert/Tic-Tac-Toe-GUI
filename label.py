from tkinter import *

class Labels:
    def __init__(self, board_instance):
        self.board_instance = board_instance
        self.turn_label = Label(self.board_instance.root,
                           text=f"It is Player 1's turn",
                           bg='gray',
                           font=('Courier', 24, 'bold'))
        self.turn_label.place(x=50, y=450)
        self.score_label = Label(self.board_instance.root,
                                 text=f"Current score: 0",
                                 bg='gray',
                                 font=('Courier', 12, 'normal'))
        self.score_label.place(x=10, y=10)
        with open('highscore.txt', 'r') as data:
            highscore = data.read()
        self.high_score_label = Label(self.board_instance.root,
                                      text=f" Highscore: {highscore}",
                                      bg= 'Gray',
                                      font=('Courier', 12, 'normal'))
        self.high_score_label.place(x=360, y=10)
