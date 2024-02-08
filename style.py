from tkinter import *

root = Tk()
root.title("Button Alignment Example")

# Create buttons
button1 = Button(root, text="Button 1")
button2 = Button(root, text="Button 2")
button3 = Button(root, text="Button 3")

# Pack buttons horizontally with padding
button1.pack(side=LEFT, padx=5, pady=10)
button2.pack(side=LEFT, padx=5, pady=10)
button3.pack(side=LEFT, padx=5, pady=10)

root.mainloop()
