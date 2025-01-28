import csv

def readData():
    movies = []
    with open('data/movieData.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            if lines[0] != "Title":
                movies.append(lines)
    return movies

def on_button_click(button_name):
    match button_name:
        case "Add":
            print("test")
        case "Info":
            print("test")
        case "Find":
            print("test")
        case "Delete":
            print("test")