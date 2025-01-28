
class Movie:
  def __init__(self, title, length, genres, year):
    self.title = title
    self.length = length
    self.genres = genres
    self.year = year

# getter and setter for Title
  def getTitle(self):
    return self.title
  
  def setTitle(self, title):
    self._title = title

# getter and setter for Length
  def getLength(self):
    return self.length
  
  def setLength(self, length):
    self._length = length

# getter and setter for Genres
  def getGenres(self):
    return self.genres
  
  def setGenres(self, genres):
    self._genres = genres
  
# getter and setter for year
  def getYear(self):
    return self.year
  
  def setYear(self, year):
    self._year = year