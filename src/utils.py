from src.property import Property

def get_properties_from_os(list_of_buildings):
    list_of_properties = []
    for i in range(len(list_of_buildings)):
        coordinates = list_of_buildings[i]["geometry"]["coordinates"][0][0]
        building = list_of_buildings[i]["properties"]
        uprn_array = building["uprnreference"]
        for j in range(len(uprn_array)):
            year = (
                "buildingage_year"
                if building["buildingage_year"]
                else "buildingage_period"
            )
            new_prop = Property(uprn_array[j]["uprn"])
            new_prop.connectivity = building["connectivity"]
            new_prop.year = building[year]
            new_prop.material = building["constructionmaterial"]
            new_prop.long = coordinates[0]
            new_prop.lat = coordinates[1]
            list_of_properties.append(new_prop)

    return list_of_properties

            






