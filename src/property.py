MINIMUM_FAILING_YEAR = 1959
CONNECTIVITY_VALUES = {
    "Standalone": "Free-Standing",
    "Semi-Connected": "Dual-Connected",
    "End-Connected": "Single-Connected",
}
WARM_MATERIALS = ["Brick Or Block Or Stone", "Contrete"]


class Property:
    def __init__(self, uprn):
        self.uprn = uprn
        self.address = ""
        self.year = 0
        self.connectivity = ""
        self.material = ""
        self.score = 0
        self.coordinates = []
        self.size = 0
        self.osid = ""
        self.age_updated_date = ""

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
        return score

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
