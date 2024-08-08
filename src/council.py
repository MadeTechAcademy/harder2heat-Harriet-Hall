from .property import Property
from mocking.french_property import FrenchProperty


class Council:
    def __init__(self, name, country):
        self.name = name
        self.list_of_properties = []
        self.country = country

    def generate_property_class_list(self, properties_data):

        for property_i in properties_data:

            property = property_i["properties"]

            year_or_period = (
                property["buildingage_year"]
                if type(property["buildingage_year"]) is int
                else property["buildingage_period"]
            )
            uprn = property["uprnreference"][0]["uprn"]
            year = year_or_period
            connectivity = property["connectivity"]
            material = property["constructionmaterial"]
            coordinates = property_i["geometry"]["coordinates"][0]
            size = property["geometry_area_m2"]
            osid = property["osid"]
            age_updated_date = property["buildingage_updatedate"]

            if self.country == "UK":
                new_property = Property(
                    uprn,
                    year,
                    connectivity,
                    material,
                    coordinates,
                    size,
                    osid,
                    age_updated_date,
                )
            elif self.country == "France":
                floors = property["number_of_floors"]
                distance_to_transport = property["distance_to_public_transport_meters"]

                new_property = FrenchProperty(
                    uprn,
                    year,
                    connectivity,
                    material,
                    coordinates,
                    size,
                    osid,
                    age_updated_date,
                    floors,
                    distance_to_transport,
                )

            self.list_of_properties.append(new_property)
            

    def get_hardest_to_heat_properties(self):
        for property in self.list_of_properties:
            property.calculate_score()
        self.list_of_properties.sort(reverse=True, key=lambda property: property.score)
