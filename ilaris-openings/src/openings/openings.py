import chess.pgn
import io
import os

class Opening:
    def __init__(self, name, game, comments):
        self.name = name
        self.game = game
        self.comments = comments

    def get_comment(self, move_index):
        return self.comments.get(move_index)

    def load_opening_from_pgn(file_path):
        with open(file_path) as f:
            game = chess.pgn.read_game(f)
            name = game.headers.get("Opening", "Unknown Opening")
            comments = {}

            node = game
            move_index = 0
            while node.variations:
                next_node = node.variation(0)
                if next_node.comment:
                    comments[move_index] = next_node.comment
                node = next_node
                move_index += 1

            return Opening(name, game, comments)
