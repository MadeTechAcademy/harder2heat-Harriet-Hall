from src.property_connectivity import Connectivity
from src.property_year import Year


MINIMUM_FAILING_YEAR = 1959
CONNECTIVITY_VALUES = {
    "Standalone": "Free-Standing",
    "Semi-Connected": "Single-Connected",
    "End-Connected": "Dual-Connected",
}
WARM_MATERIALS = ["Brick Or Block Or Stone", "Concrete"]


class Property:
    def __init__(
        self,
        uprn,
        year,
        connectivity,
        material,
        coordinates,
        size,
        osid,
        age_updated_date,
    ):
        self.uprn = uprn
        self.year = Year(year)
        self.connectivity = Connectivity(connectivity)
        self.material = material
        self.coordinates = coordinates
        self.size = size
        self.osid = osid
        self.age_updated_date = age_updated_date
        self.score = 0

    def get_year(self):
        return self.year.get_year()


    def calculate_score(self):
        year = self.get_year(self.year)
        score = 0
        if self.connectivity == "Free-Standing":
            score += 1
        if self.material not in WARM_MATERIALS:
            score += 1
        if year <= MINIMUM_FAILING_YEAR and year > 0:
            score += 1
        self.score = score
