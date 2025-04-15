from ui.main_menu import Menu
from ui.choose_opening import ChooseOpening
from ui.practice_opening import PracticeOpening

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
        self._current_view = Menu(self._root, self._show_choose_opening)
        self._current_view.pack(fill="both", expand=True)
        
    def _show_choose_opening(self):
        self._hide_current_view()
        self._current_view = ChooseOpening(self._root, self.switch_to_practice)
        self._current_view.pack(fill="both", expand=True)

    def switch_to_practice(self, opening):
        self._show_frame(PracticeOpening(self._root, opening, self._show_choose_opening))

    def _show_frame(self, frame):
        self._hide_current_view()
        self._current_view = frame
        self._current_view.pack(fill="both", expand=True)

