from ui.main_menu import Menu
from ui.choose_opening import ChooseOpening
from ui.practice_opening import PracticeOpening
from ui.login import Login
from ui.register import Register

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        
    def start(self):
        self._show_main_menu()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None
        
    def _show_main_menu(self):
        self._hide_current_view()
        self._current_view = Menu(self._root, self._show_choose_opening, self._show_login)
        self._current_view.pack(fill="both", expand=True)
        
    def _show_choose_opening(self):
        self._hide_current_view()
        self._current_view = ChooseOpening(self._root, self._show_practice_opening, self._show_main_menu)
        self._current_view.pack(fill="both", expand=True)

    def _show_practice_opening(self, opening):
        self._show_frame(PracticeOpening(self._root, opening, self._show_choose_opening))

    def _show_frame(self, frame):
        self._hide_current_view()
        self._current_view = frame
        self._current_view.pack(fill="both", expand=True)

    def _show_login(self):
        self._hide_current_view()
        self._current_view = Login(self._root, self._show_main_menu, self._show_register)
        self._current_view.pack(fill="both", expand=True)

    def _show_register(self):
        self._hide_current_view()
        self._current_view = Register(self._root, self._show_main_menu, self._show_login)
        self._current_view.pack(fill="both", expand=True)
