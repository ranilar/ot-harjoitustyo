import tkinter as tk
from PIL import Image, ImageTk
import chess # type: ignore
import chess.svg # type: ignore
 
BOARD_SIZE = 400
SQUARE_SIZE = BOARD_SIZE // 8

class ChessView:
    def __init__(self, root):
        self.root = root
        self.root.title("ilari's openings")

        self.board = chess.Board()

        self.canvas = tk.Canvas(root, width=BOARD_SIZE, height=BOARD_SIZE)
        self.canvas.pack()

        self.piece_images = self.load_piece_images()

        self.draw_board()

    def load_piece_images(self):
        pieces = {}
        piece_symbols = ['p', 'r', 'n', 'b', 'q', 'k']
        colors = ['w', 'b']

        for color in colors:
            for symbol in piece_symbols:
                filename = f"src/assets/{color}{symbol}.png"
                image = Image.open(filename).resize((SQUARE_SIZE, SQUARE_SIZE))
                pieces[color + symbol] = ImageTk.PhotoImage(image)

        return pieces

    def draw_board(self):
        colors = ["#EEEED2", "#769656"]
        for row in range(8):
            for col in range(8):
                x1, y1 = col * SQUARE_SIZE, row * SQUARE_SIZE
                x2, y2 = x1 + SQUARE_SIZE, y1 + SQUARE_SIZE
                color = colors[(row + col) % 2]
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)

        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece:
                row, col = 7 - (square // 8), square % 8
                x, y = col * SQUARE_SIZE, row * SQUARE_SIZE
                piece_key = ('w' if piece.color == chess.WHITE else 'b') + piece.symbol().lower()
                self.canvas.create_image(x, y, anchor="nw", image=self.piece_images[piece_key])

if __name__ == "__main__":
    root = tk.Tk()
    app = ChessView(root)
    root.mainloop()
