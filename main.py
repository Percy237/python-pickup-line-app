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
import sqlite3
import string
import random
import datetime


root = tb.Window(themename="darkly")
root.title("Rizz Like Percy!")
root.geometry("1000x700")

my_notebook = tb.Notebook(root, bootstyle="dark")
my_notebook.pack(pady=20)

main_tab = tb.Frame(my_notebook)
register_tab = tb.Frame(my_notebook)


# Create a function to get random pickup line
current_node = None


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
    if category_combo.get() == "Funny 😄":
        line_label.config(text=get_random_funny_pickup_line())
    elif category_combo.get() == "Flirty 😉":
        line_label.config(text=get_random_flirty_pickup_line())
    elif category_combo.get() == "Clever 🧠":
        line_label.config(text=get_random_clever_pickup_line())
    elif category_combo.get() == "Romantic 💖":
        line_label.config(text=get_random_romantic_pickup_line())
    elif category_combo.get() == "Complementary 🥰":
        line_label.config(text=get_random_complementary_pickup_line())
    elif category_combo.get() == "Cheesy 😊":
        line_label.config(text=get_random_cheesy_pickup_line())


# Creating binding function
def click_bind(e):
    line_label.config(text=f"You selected {category_combo.get()} category")
    selected_category = category_combo.get()
    category_button.config(text=f"Get random {selected_category}")


# Creating frame for my line
# line_frame = tb.Frame(root, bootstyle="darkly")
# line_frame.pack(pady=40)

# Create a label
line_label = tb.Label(
    main_tab,
    text="Rizz Like Percy 🤙😎",
    font=("Comic Sans MS", 20),
    wraplength=1000,
)
line_label.pack(pady=50)

# Creating style for my button
success_button_style = tb.Style()
success_button_style.configure("success.TButton", font=("Comic Sans MS", 20))

primary_button_style = tb.Style()
primary_button_style.configure("primary.TButton", font=("Comic Sans MS", 20))

info_button_style = tb.Style()
info_button_style.configure("info.TButton", font=("Comic Sans MS", 18))

# Frame for buttons
navigation_frame = tb.Frame(main_tab)
navigation_frame.pack(pady=20)


# Previous button
previous = tb.Button(
    navigation_frame,
    text="Previous",
    bootstyle="primary",
    command=get_previous,
    width=10,
)
previous.pack(pady=20, padx=10, side=LEFT)

# Create a button
random_button = tb.Button(
    navigation_frame,
    text="Get a random line",
    bootstyle="primary, outline",
    command=get_random,
    style="success.TButton",
    width=15,
)
random_button.pack(pady=20, padx=10, side=LEFT)

# Next button
next = tb.Button(
    navigation_frame,
    text="Next",
    bootstyle="primary, outline",
    command=get_next,
    style="primary.TButton",
    width=10,
)
next.pack(pady=20, padx=10, side=LEFT)


# Creating category options
categories = [
    "Funny 😄",
    "Cheesy 😊",
    "Flirty 😉",
    "Complementary 🥰",
    "Romantic 💖",
    "Clever 🧠",
]


# Creating Combobox
category_combo = tb.Combobox(
    main_tab, bootstyle="success", values=categories, font=("Helvetica", 18)
)
category_combo.pack(pady=20)

# Set Combo Default
category_combo.current(0)

category_button = tb.Button(
    main_tab,
    text=f"Get random {category_combo.get()}",
    command=get_random_category,
    bootstyle="info",
    style="info.TButton",
)
category_button.pack(pady=20)

# Bind the combobox
category_combo.bind("<<ComboboxSelected>>", click_bind)

my_label2 = Label(
    register_tab,
    text="You got a line in mind? Drop it below 🤙",
    font=("Helvetica", 20),
)
my_label2.pack(pady=20)

my_notebook.add(main_tab, text="Main")
my_notebook.add(register_tab, text="Enter Line")

# Creating Entry for language
language_label = Label(register_tab, text="Enter Language:", font=("Helvetica", 16))
language_label.pack(pady=20)
language_entry = tb.Entry(register_tab)
language_entry.pack(pady=20)

# Creating Entry for category
entry_categories = [
    "Funny 😄",
    "Cheesy 😊",
    "Flirty 😉",
    "Complementary 🥰",
    "Romantic 💖",
    "Clever 🧠",
]

category_label = Label(register_tab, text="Select Category", font=("Helvetica", 16))
category_label.pack(pady=10)

entry_category_combo = tb.Combobox(
    register_tab, bootstyle="success", values=entry_categories, font=("Helvetica", 18)
)
entry_category_combo.pack(pady=10)


# Creating Entry for line
entry_line_label = Label(register_tab, text="Enter Line", font=("Helvetica", 16))
entry_line_label.pack(pady=10)
line_entry = tb.Entry(register_tab)
line_entry.pack(pady=10)


def generate_random_string(length=24):
    hex_characters = string.hexdigits[
        :-6
    ]  # Only take the hex characters without 'abcdef'
    return "".join(random.choice(hex_characters) for _ in range(length))


# Generate the current date and time as a string
current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# function to save pickup_line
def save_line():
    random_string = generate_random_string()
    language = language_entry.get()
    print(language.capitalize())
    category = entry_category_combo.get()[:-2]
    print(category)
    line = line_entry.get()
    print(line)

    # Connection to db
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    language_query = "SELECT id FROM language WHERE language = ?"
    language_id = cursor.execute(language_query, (language,)).fetchone()
    if language_id is None:
        cursor.execute("INSERT INTO language(language) VALUES (?)", (language,))
        language_id = cursor.lastrowid
    else:
        language_id = language_id[0]

    category_query = "SELECT id FROM language WHERE language = ?"
    category_id = cursor.execute(category_query, (category,)).fetchone()
    if category_id is None:
        cursor.execute("INSERT INTO category(category) VALUES (?)", (category,))
        category_id = cursor.lastrowid
    else:
        category_id = category_id[0]

    cursor.execute(
        """
                INSERT INTO pickup_line(id, text, category_id, language_id, dateCreated)
                VALUES (?, ?, ?, ?, ?)
            """,
        (
            random_string,
            line,
            category_id,
            language_id,
            current_datetime,
        ),
    )

    conn.commit()
    conn.close()


# Submit button
submit_button = tb.Button(register_tab, text="Submit", command=save_line)
submit_button.pack(pady=10)


root.mainloop()
