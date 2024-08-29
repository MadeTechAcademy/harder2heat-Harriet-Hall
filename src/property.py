from src.utils import handle_connectivity, handle_year_string


MINIMUM_FAILING_YEAR = 1959
CONNECTIVITY_VALUES = {
    "Standalone": "Free-Standing",
    "Semi-Connected": "Single-Connected",
    "End-Connected": "Dual-Connected",
}
WARM_MATERIALS = ["Brick Or Block Or Stone", "Contrete"]


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
        self.year = year
        self.connectivity = connectivity
        self.material = material
        self.coordinates = coordinates
        self.size = size
        self.osid = osid
        self.age_updated_date = age_updated_date
        self.score = 0

    def calculate_score(self):
        score = 0
        year = handle_year_string(self.year)
        connectivity = handle_connectivity(self.connectivity)
        if connectivity == "Free-Standing":
            score += 1
        if self.material not in WARM_MATERIALS and self.material != "":
            score += 1
        if year <= MINIMUM_FAILING_YEAR and year > 0:
            score += 1

        self.score = score
    
