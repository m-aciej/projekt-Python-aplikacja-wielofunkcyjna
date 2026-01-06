import ttkbootstrap as tb
from ttkbootstrap.constants import LEFT, RIGHT, X, NSEW

from frames.home_frame import HomeFrame
from frames.calculator_frame import CalculatorFrame
from frames.timer_frame import TimerFrame
from frames.reader_frame import ReaderFrame
from frames.about_frame import AboutFrame

class App(tb.Window):
    APP_NAME = "Aplikacja wielofunkcyjna"

    def __init__(self):
        super().__init__(themename="flatly")

        self.title(self.APP_NAME)
        self.geometry("1000x650")
        self.minsize(860, 520)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        self.labels = {
            "HomeFrame": "Strona główna",
            "CalculatorFrame": "Kalkulator",
            "TimerFrame": "Timer",
            "ReaderFrame": "Szacowanie czasu czytania",
            "AboutFrame": "O programie"
        }

        self._create_topbar()
        self._create_content_container()
        self._create_frames()
        self.show_frame("HomeFrame")

    def _create_topbar(self) -> None:
        self.topbar = tb.Frame(self, padding=(16, 16))
        self.topbar.grid(row=0, column=0, sticky="ew")
        self.topbar.columnconfigure(0, weight=1)
        self.topbar.columnconfigure(1, weight=0)

        left = tb.Frame(self.topbar)
        left.grid(row=0, column=0, sticky="w")

        self.app_label = tb.Label(
            left,
            text = self.APP_NAME,
            font=("Segoe UI", 30, "bold"),
            justify=LEFT,
        )
        self.app_label.pack(anchor="w")

        self.module_label = tb.Label(
            left,
            text="",
            font=("Segoe UI", 13, "bold"),
            justify=LEFT,
        )
        self.module_label.pack(anchor="w", pady=(6,10))

        right = tb.Frame(self.topbar)
        right.grid(row=0, column=1, sticky="e")

        self.btn_home = tb.Button(
            right,
            text = "Home",
            bootstyle="secondary-outline",
            command = lambda: self.show_frame("HomeFrame"),
            width = 10,
        )
        self.btn_close = tb.Button(
            right,
            text = "Zamknij",
            bootstyle = "danger-outline",
            command = self.destroy,
            width = 10,
        )

        self.btn_close.pack(side=RIGHT)
        self.btn_home.pack(side=RIGHT, padx=(0, 10))

        tb.Separator(self.topbar).grid(row=1, column=0, columnspan=2, sticky="ew", pady=(6,0))

    def _create_content_container(self) -> None:
        self.content = tb.Frame(self, padding=18)
        self.content.grid(row=1, column=0, sticky = NSEW)
        self.content.rowconfigure(0, weight=1)
        self.content.columnconfigure(0, weight=1)

    def _create_frames(self) -> None:
        self.frames: dict[str, tb.Frame] = {}
        for FrameClass in (HomeFrame, CalculatorFrame, TimerFrame, ReaderFrame, AboutFrame):
            frame = FrameClass(self.content, app=self)
            name = FrameClass.__name__
            self.frames[name] = frame
            frame.grid(row=0, column=0, sticky=NSEW)

    def show_frame(self, name: str) -> None:
        frame = self.frames[name]
        frame.tkraise()

        label = self.labels.get(name, name)
        self.module_label.configure(text=label)
        self.title(f"{self.APP_NAME} - {label}")

        if name == "HomeFrame":
            if self.btn_home.winfo_ismapped():
                self.btn_home.pack(side=RIGHT, padx=(0, 10))

if __name__ == "__main__":
    app = App()
    app.mainloop()