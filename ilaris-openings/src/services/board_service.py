import io
from PIL import Image, ImageTk
import chess.svg
import chess.pgn
import cairosvg
from entities.openings import Opening

class BoardService:
    def __init__(self):
        """
        Initializes the BoardService.
        """
        self,

    def board_to_photoimage(self, board, size=400):
        """
        Converts a chess.Board object into a Tkinter PhotoImage.

        Args:
            board (chess.Board): The chess board to render.
            size (int): The pixel size of the rendered image.

        Returns:
           The rendered board image.
        """
        svg_data = chess.svg.board(board, size=size)
        png_data = cairosvg.svg2png(bytestring=svg_data.encode('utf-8'))
        image = Image.open(io.BytesIO(png_data))
        return ImageTk.PhotoImage(image)

    def load_opening_from_pgn(self, file_path):
        """
        Loads a chess opening from a PGN file, extracing its name and comments.

        Args:
            The path to the PGN file.

        Returns:
            Opening: An Opening object containing the game and comments.
        """
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
