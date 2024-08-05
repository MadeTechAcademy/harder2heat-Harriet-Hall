MINIMUM_FAILING_YEAR = 1959
CONNECTIVITY_VALUES = {
    "Standalone": "Free-Standing",
    "Semi-Connected": "Dual-Connected",
    "End-Connected": "Single-Connected",
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
        self.handle_year_string()
        self.handle_connectivity()
        if self.connectivity == CONNECTIVITY_VALUES["Standalone"]:
            score += 1
        if self.material not in WARM_MATERIALS and self.material != "":
            score += 1
        if self.year <= MINIMUM_FAILING_YEAR and self.year > 0:
            score += 1

        self.score = score
    

    def handle_year_string(self):
        if self.year == "None":
            self.year = MINIMUM_FAILING_YEAR
        year_is_int = type(self.year) is int
        if not year_is_int:
            self.year = int(self.year[-4:])

    def handle_connectivity(self):
        if self.connectivity == "Standalone":
            self.connectivity = CONNECTIVITY_VALUES["Standalone"]
        elif self.connectivity == "Semi-Connected":
            self.connectivity = CONNECTIVITY_VALUES["Semi-Connected"]
        else:
            self.connectivity = CONNECTIVITY_VALUES["End-Connected"]
