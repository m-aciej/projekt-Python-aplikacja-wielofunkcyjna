import tkinter as tk
from tkinter import ttk

class CalculatorFrame(ttk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        ttk.Label(self, text="Kalkulator", font=("TkDefaultFont", 16, "bold")).pack(anchor="w", pady=(0, 10))
        ttk.Label(self, text="(Tu wstawisz pełny kalkulator)").pack(anchor="w")