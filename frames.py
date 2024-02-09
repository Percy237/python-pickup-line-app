import tkinter as tk


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Create a container to hold different pages
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Dictionary to hold different pages
        self.frames = {}

        # Add pages to the dictionary
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # Function to show a specific page
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# Page 1
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page")
        label.pack(pady=10, padx=10)

        button1 = tk.Button(
            self, text="Go to Page One", command=lambda: controller.show_frame(PageOne)
        )
        button1.pack()

        button2 = tk.Button(
            self, text="Go to Page Two", command=lambda: controller.show_frame(PageTwo)
        )
        button2.pack()


# Page 2
class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One")
        label.pack(pady=10, padx=10)

        button = tk.Button(
            self,
            text="Go to Start Page",
            command=lambda: controller.show_frame(StartPage),
        )
        button.pack()


# Page 3
class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two")
        label.pack(pady=10, padx=10)

        button = tk.Button(
            self,
            text="Go to Start Page",
            command=lambda: controller.show_frame(StartPage),
        )
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
