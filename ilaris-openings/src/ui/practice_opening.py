import tkinter as tk
from PIL import Image, ImageTk
import chess, chess.svg, cairosvg, io, os

class PracticeOpening(tk.Frame):
    def __init__(self, master, opening, _show_choose_opening):
        super().__init__(master)
        self.opening = opening
        self.moves = list(opening.game.mainline_moves())
        self.move_index = 0
        self.board = chess.Board()
        self._show_choose_opening = _show_choose_opening

        tk.Label(self, text=opening.name, font=("Garet", 20)).pack(pady=10)

        self.board_canvas = tk.Label(self)
        self.board_canvas.pack()

        self.comment_label = tk.Label(self, text="", font=("Garet", 14), wraplength=400)
        self.comment_label.pack(pady=10)

        tk.Button(self, text="Next Move", command=self.next_move).pack(pady=10)
        tk.Button(self, text="Previous Move", command=self.previous_move).pack(pady=10)
        tk.Button(self, text="Back To Openings", command=self.back_to_openings).pack(pady=10)

        self.update_board_image()

    def update_board_image(self):
        svg_data = chess.svg.board(self.board, size=400)
        png_data = cairosvg.svg2png(bytestring=svg_data.encode('utf-8'))
        image = Image.open(io.BytesIO(png_data))
        self.board_img = ImageTk.PhotoImage(image)
        self.board_canvas.configure(image=self.board_img)

    def next_move(self):
        if self.move_index < len(self.moves) + 1:
            move = self.moves[self.move_index]
            self.board.push(move)
            self.update_board_image()

            comment = self.opening.get_comment(self.move_index)
            if comment:
                self.comment_label.config(text=f"{comment}")
            else:
                self.comment_label.config(text="")

            self.move_index += 1

    def previous_move(self):
            self.board.pop()
            self.update_board_image()

            comment = self.opening.get_comment(self.move_index)
            if comment:
                self.comment_label.config(text=f"{comment}")
            else:
                self.comment_label.config(text="")

            self.move_index -= 1
        
    def back_to_openings(self):
        self._show_choose_opening()