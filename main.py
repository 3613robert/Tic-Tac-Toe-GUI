from board import Board
from label import Labels
from game import Game
from placemarker import PlaceMarker
from score import Score

board = Board()
labels = Labels(board_instance=board)
score = Score(board_instance=board, label_instance=labels)
placemarker = PlaceMarker(board_instance=board, label_instance=labels)
game = Game(board_instance=board, placemarker_instance=placemarker, label_instance=labels, score_instance=score)

placemarker.resize_marker()
board.draw_board()
game.mouse_click_bind(canvas=board.canvas, root=board.root)
board.run()