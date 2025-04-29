import chess

class PracticeService:
    def __init__(self, opening):
        self.opening = opening
        self.moves = list(opening.game.mainline_moves())
        self.move_index = 0
        self.board = chess.Board()

    def next_move(self):
        if self.move_index < len(self.moves):
            move = self.moves[self.move_index]
            self.board.push(move)
            self.move_index += 1

    def previous_move(self):
        if self.move_index > 0:
            self.move_index -= 1
            self.board.pop()

    def get_comment(self):
        if self.move_index == 0:
            return None
        return self.opening.get_comment(self.move_index - 1)