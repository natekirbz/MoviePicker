import tkinter as tk
from tkinter import ttk
import readAndWrite as rw
from readAndWrite import *

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
    data = rw.readData()
    for i in data:
        listbox.insert(0, i[0])

frame_buttons = ttk.Frame(frame_main)
frame_buttons.grid(row=0, column=1, sticky="n", padx=10)

button1 = ttk.Button(frame_buttons, text="Add Movie", command=lambda: rw.on_button_click("Add"))
button1.pack(pady=[35,0])

button2 = ttk.Button(frame_buttons, text="Delete Movie", command=lambda: rw.on_button_click("Delete"))
button2.pack(pady=10)

button3 = ttk.Button(frame_buttons, text="Information", command=lambda: rw.on_button_click("Info"))
button3.pack()

button_below = ttk.Button(root, text="Find me a movie!", command=lambda: rw.on_button_click("Find"))
button_below.pack(pady=5)

load()
root.mainloop()