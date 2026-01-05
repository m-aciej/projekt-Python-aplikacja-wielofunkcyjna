import tkinter as tk
from tkinter import ttk

from frames.timer_frame import TimerFrame


class HomeFrame(ttk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        body = ttk.Frame(self)
        body.grid(row = 0, column = 0, sticky = "nsew")

        for r in range(2):
            body.rowconfigure(r, weight=1)
        for c in range(2):
            body.columnconfigure(c, weight=1)

        def tile(text, target, r, c):
            button = ttk.Button(body, text = text, command=lambda: app.show_frame(target))
            button.grid(row = r, column = c, sticky = "nsew", padx = 10, pady = 10, ipadx = 10, ipady = 30)

        tile("Kalkulator", "CalculatorFrame", 0, 0)
        tile("Timer", "TimerFrame", 0, 1)
        tile("Szacowanie czasu czytania", "ReaderFrame", 1, 0)
        tile("O programie", "AboutFrame", 1, 1)