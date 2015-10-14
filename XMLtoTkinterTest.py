import tkinter as tk

list = ['h','o','i']

class SimpleGridApp():
    def __init__(self):
        self.message =[]
        for i, k in enumerate(list):
            message = tk.Message(root, text=k, width=5)
            message.grid(row=i, column=0)


root = tk.Tk()
app = SimpleGridApp(root, title='Hello World')
root.mainloop()