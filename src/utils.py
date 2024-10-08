MINIMUM_FAILING_YEAR = 1959
CONNECTIVITY_VALUES = {
    "Standalone": "Free-Standing",
    "Semi-Connected": "Single-Connected",
    "End-Connected": "Dual-Connected",
}
WARM_MATERIALS = ["Brick Or Block Or Stone", "Concrete"]

class HandleYear:

    def handle_year_string(year):
        if year == "None" or year == "":
            year = MINIMUM_FAILING_YEAR
        elif type(year) is not int:
            year = int(year[-4:])
        else:
            year
        return year


class HandleConnectivity:

    def handle_connectivity(connectivity):
        if connectivity != "":
            connectivity = CONNECTIVITY_VALUES[connectivity]

        return connectivity


class SortProperties:

    def get_hardest_to_heat_properties(properties_list):
  
        properties_list.sort(reverse=True, key=lambda property: property.score)
        return properties_list
