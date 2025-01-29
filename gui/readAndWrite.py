import csv
import movie as m
from movie import *
import info
from info import *
import subprocess

def readData():
    """
    Reads and parses movie data to use.

    return: movies- A dictionary of {title, movieObject}
    """
    movies = {}
    with open('data/movieData.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        num = 0
        for lines in csvFile:
            if num != 0:
                movies[lines[0]] = Movie(lines[0], lines[1], lines[2], lines[3])
            num += 1
    return movies

def parseGenre(genres):
    return

def on_button_click(button_name):
    """
    Switch case for seeing what button was pressed in main.

    button_name: name of button pressed
    return: void
    """
    match button_name:
        case "Add":
            # subprocess.Popen(["python", "gui/info.py"])
            info.run()
        case "Info":
            info.run()
            # subprocess.Popen(["python", "gui/info.py"])
        case "Find":
            print("test")
        case "Delete":
            print("test")