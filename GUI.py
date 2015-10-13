import tkinter as tk


TITLE_FONT = ("Times", 40, "bold")

"test1234"
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.winfo_geometry()
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree):
            frame = F(container, self)
            self.frames[F] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, c):
        '''Show a frame for the given class'''
        frame = self.frames[c]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, bg="goldenrod1")
        label = tk.Label(self,bg="goldenrod1", fg="darkblue", text="Welkom bij de NS", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, bg="blue", fg="white", text="Reis Informatie",
                            command=lambda: controller.show_frame(PageOne))
        button1.config(bg="blue", fg="white")
        button1.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, bg="blue")
        label = tk.Label(self, bg="blue", text="Actuele reisinfo", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="huidig station",
                           command=lambda: controller.show_frame(PageTwo))
        button1 = tk.Button(self, text="anders",
                           command=lambda: controller.show_frame(PageThree))
        button.pack(side=tk.LEFT)
        button1.pack(side=tk.LEFT)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, bg="red")
        label = tk.Label(self, text="Informatie station Utrecht", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Terug naar startpagina",
                           command=lambda: controller.show_frame(StartPage))
        button.pack()

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, bg="red")
        label = tk.Label(self, text="Informatie station", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Terug naar startpagina",
                           command=lambda: controller.show_frame(StartPage))
        button.pack()




if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()