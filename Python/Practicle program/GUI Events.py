import tkinter as tk


from tkinter import messagebox

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Advanced GUI Event Handling")
        self.geometry("400x300")

        # Create a label
        self.label = tk.Label(self, text="Click the button below")
        self.label.pack(pady=20)

        # Create a button and bind an event to it
        self.button = tk.Button(self, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=20)

        # Create an entry widget
        self.entry = tk.Entry(self)
        self.entry.pack(pady=20)
        self.entry.bind("<Return>", self.on_enter_press)

    def on_button_click(self):
        # Handle button click event
        messagebox.showinfo("Button Clicked", "You clicked the button!")

    def on_enter_press(self, event):
        # Handle Enter key press event in the entry widget
        entered_text = self.entry.get()
        messagebox.showinfo("Entered Text", f"You entered: {entered_text}")

if __name__ == "__main__":
    app = Application()
    app.mainloop()