from src.generate_properties import GenerateProperties

class PropertyManager:
    def __init__(self, properties_data):
        self.list_of_properties = GenerateProperties.generate_property_class_list(properties_data)

    def get_hardest_to_heat_properties(self):
        for property in self.list_of_properties:
            property.calculate_score()
        self.list_of_properties.sort(reverse=True, key=lambda property: property.score)



            