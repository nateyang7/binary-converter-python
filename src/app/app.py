import tkinter as tk

class App(tk.Tk):
    """
    Classe permettant de représenter une fenêtre principale personnalisée
    """
    BACKGROUND_COLOR: str = "#252525"  # Jet black
    FOREGROUND_COLOR: str = "#FFFAFA"  # Snow

    def __init__(self) -> None:
        tk.Tk.__init__(self)
        self.geometry("700x700")
        self.info_label: tk.Frame = tk.Frame(self, bg=self.BACKGROUND_COLOR)
        self.info_label.grid(row=0, column=0, sticky='we')
        self.label: tk.Label = tk.Label(
                self.info_label, text="Enter two numbers", 
                bg=self.BACKGROUND_COLOR, fg=self.FOREGROUND_COLOR
                )
        self.label.pack(fill='x')
        self.buttons_frame: tk.Frame = tk.Frame(self)
        self.buttons_frame.grid(row=1, column=1)
        self.center_window()
        self.mainloop()

    def setup_label(self) -> None:
        """ Créer la frame pour le label """
        pass

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
