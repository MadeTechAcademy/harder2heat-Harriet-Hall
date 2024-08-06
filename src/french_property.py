from .property import Property

class FrenchProperty(Property):
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
        floors,
        distance_to_transport,
    ):
        super().__init__(
            uprn,
            year,
            connectivity,
            material,
            coordinates,
            size,
            osid,
            age_updated_date,
        )
        self.floors = floors
        self.distance_to_transport = distance_to_transport
