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

        result_properties_list.append(new_property)

    return result_properties_list
