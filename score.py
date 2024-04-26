class Score:
    def __init__(self, board_instance, label_instance):
        self.score = 0
        self.high_score = 0
        self.board_instance = board_instance
        self.label_instance = label_instance
        self.x_won = False
        self.o_won = False

    def check_win(self):
        # Check rows
        for row in self.board_instance.board:
            if all(cell == 'X' for cell in row):
                text = 'X has won'
                self.label_instance.turn_label.config(text=text)
                self.x_won = True
            elif all(cell == 'O' for cell in row):
                text = 'O has won'
                self.label_instance.turn_label.config(text=text)
                self.o_won = True
        # Check columns
        for col in range(3):
            if all(self.board_instance.board[row][col] == 'X' for row in range(3)):
                text = 'X has won'
                self.label_instance.turn_label.config(text=text)
                self.x_won = True
            elif all(self.board_instance.board[row][col] == 'O' for row in range(3)):
                text = 'O has won'
                self.label_instance.turn_label.config(text=text)
                self.o_won = True
        # Check diagonals
        if all(self.board_instance.board[i][i] == 'X' for i in range(3)):
            text = 'X has won'
            self.label_instance.turn_label.config(text=text)
            self.x_won = True
        elif all(self.board_instance.board[i][2 - i] == 'X' for i in range(3)):
            text = 'X has won'
            self.label_instance.turn_label.config(text=text)
            self.o_won = True
        elif all(self.board_instance.board[i][i] == 'O' for i in range(3)):
            text = 'O has won'
            self.label_instance.turn_label.config(text=text)
            self.x_won = True
        elif all(self.board_instance.board[i][2 - i] == 'O' for i in range(3)):
            text = 'O has won'
            self.label_instance.turn_label.config(text=text)
            self.o_won = True

    def check_draw(self):
        return all(cell == 'X' or cell == 'O' for row in self.board_instance.board for cell in row)