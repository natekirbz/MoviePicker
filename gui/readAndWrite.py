import csv

def readData():
    movies = []
    with open('data/movieData.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            if lines[0] != "Title":
                movies.append(lines)
    return movies