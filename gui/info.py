import tkinter as tk
from tkinter import ttk

def submit(entryTitle, entryTime, entryYear):
    title = entryTitle.get()
    time = entryTime.get()
    year = entryYear.get()
    print(f"Input 1: {title}, Input 2: {time}, Input 3: {year}")

def run():
    root = tk.Tk()
    root.title("Three Inputs GUI")
    root.geometry("250x250")
    root.resizable(False, False) # prevent ui issues

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky="nsew")

    title = ttk.Label(frame, text="Title:")
    title.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    entryTitle = ttk.Entry(frame)
    entryTitle.grid(row=0, column=1, padx=5, pady=5)

    time = ttk.Label(frame, text="Time:")
    time.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    entryTime = ttk.Entry(frame)
    entryTime.grid(row=1, column=1, padx=5, pady=5)

    year = ttk.Label(frame, text="Year:")
    year.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    entryYear = ttk.Entry(frame)
    entryYear.grid(row=2, column=1, padx=5, pady=5)

    submit = ttk.Button(root, text="Submit", command=lambda: 
                        submit(entryTitle, entryTime, entryYear))
    submit.grid(row=1, column=0, pady=10)


    root.mainloop()