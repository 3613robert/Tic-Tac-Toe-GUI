from tkinter import messagebox

XCORD = 115
YCORD = 110

class Game:
    def __init__(self, board_instance, placemarker_instance, label_instance, score_instance):
        self.current_player = "Player 1"
        self.board_instance = board_instance
        self.placemarker_instance = placemarker_instance
        self.label_instance = label_instance
        self.score_instance = score_instance

    def switch_player(self):
        if self.current_player == "Player 1":
            self.current_player = "Computer"
        else:
            self.current_player = "Player 1"

    def mouse_click_bind(self, canvas, root):
        while True:
            root.wait_variable(self.board_instance.canvas.bind("<Button-1>", lambda event: self.turn(canvas, *self.mouse_click(event))))

    def reset_board(self):
        self.label_instance.score_label.config(text=f"Your score is: {self.score_instance.score}")
        again = messagebox.askquestion(title='New Game', message="Would you like to play a new game?")
        if again:
            self.board_instance.clear_board()
            self.board_instance.canvas.delete("all")
            self.board_instance.draw_board()
            self.label_instance.turn_label.config(text=f"{self.current_player} their turn")
            self.score_instance.x_won = False
            with open('highscore.txt', 'r') as data:
                highscore = data.read()
                self.score_instance.high_score = highscore
            if int(highscore) < self.score_instance.score:
                with open('highscore.txt', 'w') as data:
                    data.write(str(self.score_instance.score))
            self.label_instance.high_score_label.config(text=f"Highscore:{self.score_instance.high_score}")

    def turn(self, canvas, xcord, ycord):
        x, o = self.placemarker_instance.get_markers()
        if self.current_player == "Player 1":
            self.board_instance.canvas.create_image(xcord, ycord, image=x)
            self.switch_player()
            self.label_instance.turn_label.config(text=f"{self.current_player} their turn")
        elif self.current_player == "Computer":
            self.board_instance.canvas.create_image(xcord, ycord, image=o)
            self.switch_player()
            self.label_instance.turn_label.config(text=f"{self.current_player} their turn")
        self.score_instance.check_win()
        if self.score_instance.x_won or self.score_instance.check_draw():
            self.score_instance.score += 1
            self.reset_board()
        elif self.score_instance.o_won:
            self.score_instance.score -= 1
            if self.score_instance.score <= 0:
                self.score_instance.score = 0
            self.label_instance.score_label.config(text=f"Your score is: {self.score_instance.score}")
            again = messagebox.askquestion(title='New Game', message="Would you like to play a new game?")
            if again:
                self.board_instance.clear_board()
                self.board_instance.canvas.delete("all")
                self.board_instance.draw_board()
                self.label_instance.turn_label.config(text=f"{self.current_player} their turn")
                self.score_instance.o_won = False

    def mouse_click(self, event):
        # Calculate the cell index based on the click coordinates
        cell_row = (event.y - 50) // 120
        cell_col = (event.x - 50) // 130

        # Check if the clicked cell is empty
        if self.board_instance.board[cell_row][cell_col] == '' and cell_col != -1:
            # Place the marker in the clicked cell and return its coordinates
            if self.current_player == "Player 1":
                self.board_instance.board[cell_row][cell_col] = 'X'
            else:
                self.board_instance.board[cell_row][cell_col] = 'O'
            return [XCORD + cell_col * 130, YCORD + cell_row * 120]
        else:
            # Show a message indicating that the cell is already occupied
            messagebox.showinfo("Invalid Move", "This cell is already occupied.")
            return None  # Return None if the move is invalid