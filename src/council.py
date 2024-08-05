from src.property import Property

class Council:
    def __init__(self, name):
        self.name = name
        self.list_of_properties = []



    def generate_property_class_list(self, properties_data):
        for property_i in properties_data:

            property = property_i["properties"]

            year = (
                "buildingage_year"
                if "buildingage_year" != "None"
                else "buildingage_period"
            )
            urpn = property["uprnreference"][0]["uprn"]
            year = property[year]
            connectivity = property["connectivity"]
            material = property["constructionmaterial"]
            coordinates = property_i["geometry"]["coordinates"][0]
            size = property["geometry_area_m2"]
            osid = property["osid"]
            age_updated_date = property["buildingage_updatedate"]
            new_property = Property(
                urpn,
                year,
                connectivity,
                material,
                coordinates,
                size,
                osid,
                age_updated_date,
            )

            self.list_of_properties.append(new_property)


    def get_hardest_to_heat_properties(self):
        for property in self.list_of_properties:
            property.calculate_score()
        self.list_of_properties.sort(reverse=True, key= lambda property: property.score)
        
