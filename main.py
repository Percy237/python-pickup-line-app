from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from pickup_lines import get_random_pickup_line
from pickup_lines import get_random_funny_pickup_line
from pickup_lines import get_random_flirty_pickup_line
from pickup_lines import get_random_clever_pickup_line
from pickup_lines import get_random_romantic_pickup_line
from pickup_lines import get_random_complementary_pickup_line
from pickup_lines import get_random_cheesy_pickup_line
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


# Creating function for a random category
def get_random_category():
    if category_combo.get() == "Funny":
        line_label.config(text=get_random_funny_pickup_line())
    elif category_combo.get() == "Flirty":
        line_label.config(text=get_random_flirty_pickup_line())
    elif category_combo.get() == "Clever":
        line_label.config(text=get_random_clever_pickup_line())
    elif category_combo.get() == "Romantic":
        line_label.config(text=get_random_romantic_pickup_line())
    elif category_combo.get() == "Complementary":
        line_label.config(text=get_random_complementary_pickup_line())
    elif category_combo.get() == "Cheesy":
        line_label.config(text=get_random_cheesy_pickup_line())


# Creating binding function
def click_bind(e):
    line_label.config(text=f"You clicked on {category_combo.get()}")


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

# Creating category options
categories = ["Funny", "Cheesy", "Flirty", "Complementary", "Romantic", "Clever"]

# Creating Combobox
category_combo = tb.Combobox(root, bootstyle="success", values=categories)
category_combo.pack(pady=20)

# Set Combo Default
category_combo.current(0)

category_button = tb.Button(
    root,
    text=f"Get random",
    command=get_random_category,
    bootstyle="info",
)
category_button.pack(pady=20)

# Bind the combobox
category_combo.bind("<<ComboboxSelected>>", click_bind)

root.mainloop()
