import tkinter as tk

class App(tk.Tk):
    """
    Classe permettant de représenter une fenêtre principale personnalisée
    """
    BACKGROUND_COLOR: str = "#252525"  # Jet black
    FOREGROUND_COLOR: str = "#FFFAFA"  # Snow

    def __init__(self) -> None:
        tk.Tk.__init__(self)
        #self.geometry("700x700")
        self.info_label: tk.Frame = tk.Frame(self, bg=self.BACKGROUND_COLOR)
        #self.info_label.grid(row=0, column=0, sticky='we')
        self.info_label.pack(fill='x')
        self.label: tk.Label = tk.Label(
                self.info_label, text="Enter two numbers", 
                bg=self.BACKGROUND_COLOR, fg=self.FOREGROUND_COLOR
                )
        self.label.pack(fill='x')
        self.entry: tk.Entry = tk.Entry(self, bg='grey')
        self.entry.pack()
        self.buttons_frame: tk.Frame = tk.Frame(self, bg="blue")
        self.buttons_frame.pack(side="bottom", fill='x')
        #self.buttons_frame.grid(row=1, column=1)
        self.setup_buttons(4, 4)
        self.center_window()
        self.mainloop()

    def setup_buttons(self, rows: int, cols: int) -> None:
        """ Créer et organise la frame des boutons """
        buttons_grid: list[list[int]] = [
            [0] * cols for _ in range(rows)
        ]
        for row in range(rows):
            for column in range(cols):
                print(row, column)
                button: tk.Button = tk.Button(self.buttons_frame, text='x')
                buttons_grid[row][column] = button
                buttons_grid[row][column].grid(row=row, column=column)

    def center_window(self) -> None:
        """ Centre la fenêtre principale """
        self.update()
        window_width: int = self.winfo_width()
        window_height: int = self.winfo_height()
        screen_width: int = self.winfo_screenwidth()
        screen_height: int = self.winfo_screenheight()
        x: int = int((1 / 2) * (screen_width - window_width))
        y: int = int((1 / 2) * (screen_height - window_height))
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")


if __name__ == "__main__":
    APP_TEST = App()
