from ui.ui import UI
import tkinter as tk

def main():
    window = tk.Tk()
    window.title("ilari's openings")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()

if __name__ == "__main__":
    main()
