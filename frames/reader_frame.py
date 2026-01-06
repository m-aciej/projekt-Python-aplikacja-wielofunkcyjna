import tkinter as tk
from tkinter import ttk

class ReaderFrame(ttk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        topbar = ttk.Frame(self)
        topbar.grid(row=0, column=0, sticky="ew", pady=(0, 12))
        topbar.columnconfigure(1, weight=1)

        body = ttk.Frame(self)
        body.grid(row=1, column=0, sticky="nsew")