import tkinter as tk
from tkinter import ttk
import readAndWrite as rw
from readAndWrite import *
import info
from info import *

root = tk.Tk()
root.title("Movie Picker")
root.geometry("250x250")
root.resizable(False, False) # prevent ui issues

label_title = ttk.Label(root, text="Movie Picker", font=(16))
label_title.pack(pady=10)

frame_main = ttk.Frame(root)
frame_main.pack(fill=tk.BOTH)

listbox = tk.Listbox(frame_main, height=10)
listbox.grid(row=0, column=0, sticky="ns", padx=[10,0])

def load():
    """
    Calls read data from readAndWrite to get movie data.

    return: void
    """
    data = rw.readData()
    for key in data:
        listbox.insert(0, key)

frame_buttons = ttk.Frame(frame_main)
frame_buttons.grid(row=0, column=1, sticky="n", padx=10)

button1 = ttk.Button(frame_buttons, text="Add Movie", command=lambda: rw.on_button_click("Add"))
button1.pack(pady=[35,0])

button2 = ttk.Button(frame_buttons, text="Delete Movie", command=lambda: rw.on_button_click("Delete"))
button2.config(state=tk.DISABLED)
button2.pack(pady=10)

button3 = ttk.Button(frame_buttons, text="Information", command=lambda: rw.on_button_click("Info"))
button3.config(state=tk.DISABLED)
button3.pack()

button_below = ttk.Button(root, text="Find me a movie!", command=lambda: rw.on_button_click("Find"))

# disable find button if no movies in data
if (not bool(rw.readData())):
    button_below.config(state=tk.DISABLED)
else:
    button_below.config(state=tk.NORMAL)
button_below.pack(pady=5)

# 
def on_select(event):
    """
    on_select changes button states for info and delete.

    event: unused
    return: void
    """
    button3.config(state=tk.NORMAL)
    button2.config(state=tk.NORMAL)
    movie = listbox.curselection()
    if movie:
        title = listbox.get(movie[0])
        print(f"Selected: {title}")

listbox.bind("<<ListboxSelect>>", on_select)

load()
root.mainloop()