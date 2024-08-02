from src.property import Property


def generate_property_class_list(list_of_properties):
    result_properties_list = []

    for property_i in list_of_properties:
        property = property_i["properties"]
        year = (
            property["buildingage_year"]
            if property["buildingage_year"] != "None"
            else "buildingage_period"
        )
        new_property = Property(property["uprnreference"][0]["uprn"])
        new_property.coordinates = property_i["geometry"]["coordinates"][0]
        new_property.connectivity = property["connectivity"]
        new_property.year = property[year]
        new_property.material = property["constructionmaterial"]
        new_property.age_updated_date = property["buildingage_updatedate"]
        new_property.size = property["geometry_area_m2"]
        new_property.osid = property["osid"]

        result_properties_list.append(new_property)

    return result_properties_list
