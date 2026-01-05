import ttkbootstrap as tb
from ttkbootstrap.constants import LEFT, RIGHT, BOTH, X, Y, NS, NSEW, TOP

from frames.home_frame import HomeFrame
from frames.calculator_frame import CalculatorFrame
from frames.timer_frame import TimerFrame
from frames.reader_frame import ReaderFrame
from frames.about_frame import AboutFrame

class App(tb.Window):
    def __init__(self):
        super().__init__(themename="flatly")

        self.title("Aplikacja wielofunkcyjna")
        self.geometry("1000x650")
        self.minsize(860, 520)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.labels = {
            "HomeFrame": "Strona główna",
            "CalculatorFrame": "Kalkulator",
            "TimerFrame": "Timer",
            "ReaderFrame": "Szacowanie czasu czytania",
            "AboutFrame": "O programie",
        }

        self._nav_buttons: dict[str, tb.Button] = {}

        self._create_sidebar()
        self._create_container()
        self._create_frames()
        self.show_frame("HomeFrame")

    def _create_sidebar(self) -> None:
        self.sidebar = tb.Frame(self, padding=(14, 16))
        self.sidebar.grid(row = 0, column = 0, sticky= NS)

        self.sidebar.grid_propagate(False)
        self.sidebar.configure(width=260)

        title = tb.Label(
            self.sidebar,
            text="Aplikacja\nwielofunkcyjna",
            font=("Segoe UI", 16, "bold"),
            justify=LEFT
        )
        title.pack(anchor="w", pady=(0, 14))

        subtitle = tb.Label(
            self.sidebar,
            text = "Wybierz moduł",
            font = ("Segoe UI", 10),
        )
        subtitle.pack(anchor="w", pady=(0, 18))

        nav = tb.Frame(self.sidebar)
        nav.pack(fill=X, expand=False)

        nav_items = [
            ("HomeFrame", "Strona główna"),
            ("CalculatorFrame", "Kalkulator"),
            ("TimerFrame", "Timer"),
            ("ReaderFrame", "Szacowanie czasu czytania"),
            ("AboutFrame", "O programie"),
        ]

        for frame_name, text in nav_items:
            btn = tb.Button(
                nav,
                text = text,
                bootstyle="secondary-outline",
                command=lambda n = frame_name: self.show_frame(n),
                width=24,
            )
            btn.pack(fill=X, pady=6)
            self._nav_buttons[frame_name] = btn

        tb.Separator(self.sidebar).pack(fill=X, pady=(18, 14))

        quit_btn = tb.Button(
            self.sidebar,
            text="Zamknij program",
            bootstyle="danger",
            command=self.destroy,
        )
        quit_btn.pack(side=TOP, fill=X)

    def _create_container(self) -> None:
        self.container = tb.Frame(self, padding=18)
        self.container.grid(row=0, column=1, sticky=NSEW)
        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)

    def _create_frames(self) -> None:
        self.frames: dict[str, tb.Frame] = {}
        for FrameClass in (HomeFrame, CalculatorFrame, TimerFrame, ReaderFrame, AboutFrame):
            frame = FrameClass(self.container, app=self)
            name = FrameClass.__name__
            self.frames[name] = frame
            frame.grid(row=0, column=0, sticky=NSEW)

    def show_frame(self, name: str) -> None:
        frame = self.frames[name]
        frame.tkraise()

        label = self.labels.get(name, name)
        self.title(f"Aplikacja wielofunkcyjna - {label}")

        for frame_name, btn in self._nav_buttons.items():
            if frame_name == name:
                btn.configure(bootstyle="primary")
            else:
                btn.configure(bootstyle="secondary-outline")

if __name__ == "__main__":
    app = App()
    app.mainloop()