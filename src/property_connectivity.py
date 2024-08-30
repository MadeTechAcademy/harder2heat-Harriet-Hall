CONNECTIVITY_VALUES = {
    "Standalone": "Free-Standing",
    "Semi-Connected": "Single-Connected",
    "End-Connected": "Dual-Connected",
}
class Connectivity:
  def __init__(self, connectivity):
    self._connectivity = self.handle_connectivity(connectivity) 
    
  def handle_connectivity(self, connectivity):
      if connectivity is not "":
           connectivity = CONNECTIVITY_VALUES[connectivity]
     
      return connectivity

  def get_connectivity(self):
        return self._connectivity
