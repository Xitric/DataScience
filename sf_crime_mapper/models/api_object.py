from datetime import datetime


class ApiObject:
    TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
    RESOURCE_ID = ""

    @classmethod
    def from_dictionary(cls, dictionary):
        pass

    @staticmethod
    def to_struct_time(string_time):
        return datetime.strptime(string_time, ApiObject.TIME_FORMAT)

    @staticmethod
    def date_name():
        pass

    def date(self):
        pass
