MINIMUM_FAILING_YEAR = 1959


class Year:
  def __init__(self, year):
    self.year = self.handle_year_string(year) 
    
  def handle_year_string(self, year):
      if year == "None" or year == "":
          year = MINIMUM_FAILING_YEAR
      elif type(year) is not int:
          year = int(year[-4:])
      else:   
          year
      return year
