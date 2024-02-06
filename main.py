from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from pickup_lines import get_random_pickup_line
from linkedlist import Line

current_node = None


# Create a function to get random pickup line
def get_random():
    global current_node
    line = get_random_pickup_line()
    node = Line(line=line, prev=current_node)
    if current_node is not None:
        next_node = current_node.next
        current_node.next = node
        node.next = next_node
    current_node = node
    print(f"Current node is: {current_node}")
    print(f"Previous node is: {current_node.prev}")
    line_label.config(text=line)


def get_previous():
    global current_node
    if current_node is not None:
        current_node = (
            current_node.prev if current_node.prev is not None else current_node
        )
        line_label.config(text=current_node.line)
    else:
        print("There's no current node")


def get_next():
    global current_node
    if current_node is not None:
        current_node = (
            current_node.next if current_node.next is not None else current_node
        )
        line_label.config(text=current_node.line)
    else:
        print("There's no current node")


root = tb.Window(themename="darkly")
root.title("Rizz Like Percy!")
root.geometry("500x350")

# Creating frame for my line
line_frame = tb.Frame(root, bootstyle="darkly")
line_frame.pack(pady=40)

# Create a label
line_label = tb.Label(line_frame, text="Rizz Like Percy!", font=("Hevelica", 20))
line_label.pack(pady=30)

# Creating style for my button

my_style = tb.Style()
my_style.configure("success.TButton", font=("Helvetica", 18))

# Create a button
random_button = tb.Button(
    text="Get a random one",
    bootstyle="primary, outline",
    command=get_random,
    style="my.TButton",
)
random_button.pack(pady=50)

next = tb.Button(
    text="Next",
    bootstyle="primary, outline",
    command=get_next,
)
next.pack(pady=10)
previous = tb.Button(
    text="Previous",
    bootstyle="primary, outline",
    command=get_previous,
)
previous.pack(pady=10)


root.mainloop()
