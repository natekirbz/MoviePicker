import tkinter as tk
from tkinter import *
from readAndWrite import *

root = tk.Tk()
root.title("Movie Selecter")
root.geometry("250x300")
root.resizable(False, False)


        

listbox = tk.Listbox(root, height = 10, 
                  width = 25, 
                  bg = "grey",
                  activestyle = 'dotbox', 
                  fg = "black")

# Load movie data into the listBox
def load():
    data = readData()
    for i in data:
        listbox.insert(0, i[0])

def on_click():
    # not implimented
    return

btnAdd = tk.Button(root, text="Add Movie")
btnDelete = tk.Button(root, text="Delete Movie")
btnFind = tk.Button(root, text="Find Me A Movie", command=on_click)
lblMovies = tk.Label(root, text = "List of Movies")



# Add widgets to the gui
btnFind.grid(row=4,column=0, columnspan=2)
listbox.grid(row=1,column=0,rowspan=3,sticky=EW)
lblMovies.grid(row=0,column=0)
btnAdd.grid(row=1,column=1)
btnDelete.grid(row=2,column=1)




load()
root.mainloop()