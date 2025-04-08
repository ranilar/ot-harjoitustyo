from ui.main_menu import Menu
from ui.choose_opening import ChooseOpening
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
        self._current_view = ChooseOpening(self._root)
        self._current_view.pack(fill="both", expand=True)
