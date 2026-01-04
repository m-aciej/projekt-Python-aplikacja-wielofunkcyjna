import tkinter as tk
from tkinter import ttk

class HomeFrame(ttk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        ttk.Label(self, text = "Strona główna", font=("TkDefaultFont", 16, "bold")).grid(
            row = 0, column = 0, sticky = "w", pady = (0, 12)
        )

        titles = ttk.Frame(self)
        titles.grid(row = 1, column = 0, sticky = "nsew")
        for r in range(2):
            titles.rowconfigure(r, weight=1)
        for c in range(2):
            titles.columnconfigure(c, weight=1)

        def tile(text, target, r, c):
            ttk.Button(titles, text = text, command = lambda:
                       app.show_frame(target)).grid(
                row = r, column = c, sticky = "nsew", padx = 10, pady = 10, ipadx = 10, ipady = 30
            )
        tile("Kalkulator", "CalculatorFrame", 0, 0)
        tile("Timer", "TimerFrame", 0, 1)
        tile("Szacowanie czasu czytania", "ReaderFrame", 1, 0)
        tile("O programie", "AboutFrame", 1, 1)