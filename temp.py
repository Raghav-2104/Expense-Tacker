import tkinter as tk

class button(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Button")
        self.geometry("500x500")
        self.create_widgets()

    def create_widgets(self):
        self.button = tk.Button(self, text="Click Me", command=self.click)
        self.button.pack()

    def click(self):
        self.button["text"] = "Clicked"

if __name__ == "__main__":
    app = button()
    app.mainloop()