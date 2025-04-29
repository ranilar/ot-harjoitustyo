import tkinter as tk
from services.practice_service import PracticeService
from services.board_service import BoardService

class PracticeOpening(tk.Frame):
    def __init__(self, master, opening, _show_choose_opening):
        super().__init__(master)
        self.practice_service = PracticeService(opening)
        self.board_service = BoardService
        self._show_choose_opening = _show_choose_opening


        tk.Label(self, text=opening.name, font=("Garet", 20)).pack(pady=10)

        self.board_canvas = tk.Label(self)
        self.board_canvas.pack()

        self.comment_label = tk.Label(self, text="", font=("Garet", 14), wraplength=400)
        self.comment_label.pack(pady=10)

        tk.Button(self, text="Next Move", command=self.next_move).pack(pady=10)
        tk.Button(self, text="Previous Move", command=self.prev_move).pack(pady=10)
        tk.Button(self, text="Back To Openings", command=self._show_choose_opening).pack(pady=10)
        
        self.update_board()

    def update_board(self):
        img = self.board_service.board_to_photoimage(self.practice_service.board)
        self.board_canvas.configure(image=img)
        self.board_canvas.image = img

        comment = self.practice_service.get_comment()
        self.comment_label.config(text=comment or "")

    def next_move(self):
        self.practice_service.next_move()
        self.update_board()

    def prev_move(self):
        self.practice_service.previous_move()
        self.update_board()