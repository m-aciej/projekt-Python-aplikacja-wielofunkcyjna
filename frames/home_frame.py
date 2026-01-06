import ttkbootstrap as tb
from ttkbootstrap.constants import NSEW


class HomeFrame(tb.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        body = tb.Frame(self)
        body.grid(row=0, column=0, sticky=NSEW)

        for r in range(2):
            body.rowconfigure(r, weight=1)
        for c in range(2):
            body.columnconfigure(c, weight=1)

        # Styl przycisków-kafli (większe napisy + większy "oddech")
        style = tb.Style()
        style.configure(
            "Tile.TButton",
            font=("Segoe UI", 16, "bold"),   # <-- tu zmieniasz rozmiar napisów w kafelkach
            padding=(18, 18),               # wewnętrzny odstęp (zastępuje ipadx/ipady)
        )

        def tile(text, target, r, c, bootstyle="secondary"):
            btn = tb.Button(
                body,
                text=text,
                command=lambda t=target: self.app.show_frame(t),
                bootstyle=bootstyle,          # np. "primary", "secondary", "info", "success"
                style="Tile.TButton",
                cursor="hand2",
            )
            btn.grid(row=r, column=c, sticky=NSEW, padx=10, pady=10)

        tile("Kalkulator", "CalculatorFrame", 0, 0, bootstyle="primary")
        tile("Timer", "TimerFrame", 0, 1, bootstyle="info")
        tile("Szacowanie czasu czytania", "ReaderFrame", 1, 0, bootstyle="secondary")
        tile("O programie", "AboutFrame", 1, 1, bootstyle="success")