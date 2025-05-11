import tkinter as tk
from ui.ui import UI
from initialize_database import initialize_database

def main():
    """
    Main function initializes the database and starts the UI.
    """
    window = tk.Tk()
    window.title("ilari's openings")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()

    initialize_database()

if __name__ == "__main__":
    main()
