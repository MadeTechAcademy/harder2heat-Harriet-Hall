from src.french_property import FrenchProperty

class GenerateFrenchProperties:
        
    def generate_property_class_list(properties_data):

        list_of_properties = []
        for property_data in properties_data:

            property = property_data["properties"]

            year_or_period = (
                property["buildingage_year"]
                if type(property["buildingage_year"]) is int
                else property["buildingage_period"]
            )

            uprn = property["uprnreference"][0]["uprn"]
            year = year_or_period
            connectivity = property["connectivity"]
            material = property["constructionmaterial"]
            coordinates = property_data["geometry"]["coordinates"][0]
            size = property["geometry_area_m2"]
            osid = property["osid"]
            age_updated_date = property["buildingage_updatedate"]
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
                distance_to_transport
            )

            list_of_properties.append(new_property)
            
        return list_of_properties
