import chess.svg, cairosvg, io
from entities.openings import Opening
from PIL import Image, ImageTk

class BoardService:
    def __init__(self):
        self,

    def board_to_photoimage(board, size=400):
        svg_data = chess.svg.board(board, size=size)
        png_data = cairosvg.svg2png(bytestring=svg_data.encode('utf-8'))
        image = Image.open(io.BytesIO(png_data))
        return ImageTk.PhotoImage(image)

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