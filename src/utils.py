MINIMUM_FAILING_YEAR = 1959
CONNECTIVITY_VALUES = {
    "Standalone": "Free-Standing",
    "Semi-Connected": "Single-Connected",
    "End-Connected": "Dual-Connected",
}

def handle_year_string(year):
      if year == "None" or year == "":
          year = MINIMUM_FAILING_YEAR
      elif type(year) is not int:
          year = int(year[-4:])
      else:   
          year
      return year


def handle_connectivity(connectivity):
    connectivity = CONNECTIVITY_VALUES[connectivity]
    return connectivity
    