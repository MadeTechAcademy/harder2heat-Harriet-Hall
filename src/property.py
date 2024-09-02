from .utils import HandleConnectivity, HandleYear

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
        self.year = HandleYear.handle_year_string(year)
        self.connectivity = HandleConnectivity.handle_connectivity(connectivity)
        self.material = material
        self.coordinates = coordinates
        self.size = size
        self.osid = osid
        self.age_updated_date = age_updated_date
        self.score = 0


    def calculate_score(self):
        
        score = 0
        if self.connectivity == "Free-Standing":
            score += 1
        if self.material not in WARM_MATERIALS:
            score += 1
        if self.year <= MINIMUM_FAILING_YEAR and self.year > 0:
            score += 1
        self.score = score
