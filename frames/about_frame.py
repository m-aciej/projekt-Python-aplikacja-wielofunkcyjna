import tkinter as tk
from tkinter import ttk

class AboutFrame(ttk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        ttk.Label(self, text="O programie", font=("TkDefaultFont", 16, "bold")).pack(anchor="w", pady=(0, 10))
        ttk.Label(self, text="Aplikacja wielofunkcyjna w Tkinter — menu + kafelki.").pack(anchor="w")