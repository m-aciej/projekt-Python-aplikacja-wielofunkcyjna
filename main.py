import tkinter as tk
from tkinter import ttk

from frames.home_frame import HomeFrame
from frames.calculator_frame import CalculatorFrame
from frames.timer_frame import TimerFrame
from frames.reader_frame import ReaderFrame
from frames.about_frame import AboutFrame

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplikacja wielofunkcyjna")
        self.geometry("900x600")
        self.minsize(740, 400)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight = 0)

        self.labels = {
            "HomeFrame": "Strona główna",
            "CalculatorFrame": "Kalkulator",
            "TimerFrame": "Timer",
            "ReaderFrame": "Szacowanie czasu czytania",
            "AboutFrame": "O programie",
        }

        self.status_aplikacji = tk.StringVar(value = "Gotowe")
        status = ttk.Label(self, textvariable=self.status_aplikacji, anchor="w", padding=(8,4))
        status.grid(row = 1, column = 0, sticky = "ew")

        self._create_menu()
        self._create_container()
        self.show_frame("HomeFrame")

    def _create_menu(self):
        menubar = tk.Menu(self)
        menu = tk.Menu(menubar, tearoff=False)
        menu.add_command(label="Strona główna", command=lambda: self.show_frame("HomeFrame"))
        menu.add_command(label="Kalkulator", command=lambda: self.show_frame("CalculatorFrame"))
        menu.add_command(label="Timer", command=lambda: self.show_frame("TimerFrame"))
        menu.add_command(label="Szacowanie czasu czytania", command=lambda: self.show_frame("ReaderFrame"))
        menu.add_command(label="O programie", command=lambda: self.show_frame("AboutFrame"))

        menubar.add_cascade(label="Menu", menu=menu)
        self.config(menu=menubar)

    def ustaw_status(self, text: str):
        self.status_aplikacji.set(text if text else " ")

    def show_frame(self, name: str):
        frame = self.frames[name]
        frame.tkraise()
        self.ustaw_status(self.labels.get(name, name))

    def _create_container(self):
        self.container = ttk.Frame(self, padding=12)
        self.container.grid(row = 0, column = 0, sticky = "nsew")
        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)

        self.frames = {}
        for FrameClass in (HomeFrame, CalculatorFrame, TimerFrame, ReaderFrame, AboutFrame):
            frame = FrameClass(self.container, app = self)
            name = FrameClass.__name__
            self.frames[name] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

if __name__ == "__main__":
    app = App()
    app.mainloop()