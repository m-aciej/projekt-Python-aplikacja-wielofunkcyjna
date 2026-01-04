import tkinter as tk
from tkinter import ttk

class TimerFrame(ttk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        ttk.Label(self, text="Timer", font=("TkDefaultFont", 16, "bold")).pack(anchor="w", pady=(0, 10))
        ttk.Label(self, text="(Tu wstawisz minutnik/stoper)").pack(anchor="w")