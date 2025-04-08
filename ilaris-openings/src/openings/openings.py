import chess.pgn
import io
import os

class Opening:
    def __init__(self, name, game, tips):
        self.name = name
        self.game = game
        self.tips = tips

    def get_tip(self, move_index):
        return self.tips.get(move_index)

def load_opening_from_pgn(file_path):
    with open(file_path) as f:
        game = chess.pgn.read_game(f)
        name = game.headers.get("Opening", "Unknown Opening")
        tips = {}

        for key in game.headers:
            if key.startswith("Tip"):
                try:
                    move_index = int(key[3:]) - 1
                    tips[move_index] = game.headers[key]
                except ValueError:
                    continue

        return Opening(name, game, tips)
