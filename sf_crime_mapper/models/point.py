class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_dictionary(cls, dictionary):
        coordinates = dictionary.get("coordinates")
        if coordinates:
            return cls(coordinates[0], coordinates[1])

        return None
