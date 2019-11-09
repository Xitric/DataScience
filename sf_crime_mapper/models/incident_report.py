from sf_crime_mapper.models.point import Point
from sf_crime_mapper.models.api_object import ApiObject


class HistoricalIncidentReport(ApiObject):
    """Representation of a police incident report between 2003 and 2018"""

    RESOURCE_ID = "tmnf-yvry"

    def __init__(self, incidntnum, category, descript, dayofweek, date, time, pddistrict, resolution, address, x, y,
                 location, pdid):
        self.incidntnum = incidntnum
        self.category = category
        self.descript = descript
        self.dayofweek = dayofweek
        self.date = date
        self.time = time
        self.pddistrict = pddistrict
        self.resolution = resolution
        self.address = address
        self.x = x
        self.y = y
        self.location = location
        self.pdid = pdid

    @classmethod
    def from_dictionary(cls, dictionary):
        return cls(dictionary.get("incidntnum"),
                   dictionary.get("category"),
                   dictionary.get("descript"),
                   dictionary.get("dayofweek"),
                   dictionary.get("date"),
                   dictionary.get("time"),
                   dictionary.get("pddistrict"),
                   dictionary.get("resolution"),
                   dictionary.get("address"),
                   dictionary.get("x"),
                   dictionary.get("y"),
                   Point.from_dictionary(dictionary.get("location", {})),
                   dictionary.get("pdid"))

    @staticmethod
    def date_name():
        return "date"

    def date(self):
        return self.to_struct_time(self.date)


class IncidentReport(ApiObject):
    """Representation of a police incident report since 2018"""

    RESOURCE_ID = "wg3w-h783"

    def __init__(self, incident_datetime, incident_date, incident_time, incident_year, incident_day_of_week,
                 report_datetime, row_id, incident_id, incident_number, cad_number, report_type_code,
                 report_type_description, filed_online, incident_code, incident_category, incident_subcategory,
                 incident_description, resolution, intersection, cnn, police_district, analysis_neighborhood,
                 supervisor_district, latitude, longitude, point):
        self.incident_datetime = incident_datetime
        self.incident_date = incident_date
        self.incident_time = incident_time
        self.incident_year = incident_year
        self.incident_day_of_week = incident_day_of_week
        self.report_datetime = report_datetime
        self.row_id = row_id
        self.incident_id = incident_id
        self.incident_number = incident_number
        self.cad_number = cad_number
        self.report_type_code = report_type_code
        self.report_type_description = report_type_description
        self.filed_online = filed_online
        self.incident_code = incident_code
        self.incident_category = incident_category
        self.incident_subcategory = incident_subcategory
        self.incident_description = incident_description
        self.resolution = resolution
        self.intersection = intersection
        self.cnn = cnn
        self.police_district = police_district
        self.analysis_neighborhood = analysis_neighborhood
        self.supervisor_district = supervisor_district
        self.latitude = latitude
        self.longitude = longitude
        self.point = point

    @classmethod
    def from_dictionary(cls, dictionary):
        return cls(dictionary.get("incident_datetime"),
                   dictionary.get("incident_date"),
                   dictionary.get("incident_time"),
                   dictionary.get("incident_year"),
                   dictionary.get("incident_day_of_week"),
                   dictionary.get("report_datetime"),
                   dictionary.get("row_id"),
                   dictionary.get("incident_id"),
                   dictionary.get("incident_number"),
                   dictionary.get("cad_number"),
                   dictionary.get("report_type_code"),
                   dictionary.get("report_type_description"),
                   dictionary.get("filed_online"),
                   dictionary.get("incident_code"),
                   dictionary.get("incident_category"),
                   dictionary.get("incident_subcategory"),
                   dictionary.get("incident_description"),
                   dictionary.get("resolution"),
                   dictionary.get("intersection"),
                   dictionary.get("cnn"),
                   dictionary.get("police_district"),
                   dictionary.get("analysis_neighborhood"),
                   dictionary.get("supervisor_district"),
                   dictionary.get("latitude"),
                   dictionary.get("longitude"),
                   Point.from_dictionary(dictionary.get("point", {})))

    @staticmethod
    def date_name():
        return "report_datetime"

    def date(self):
        return self.to_struct_time(self.report_datetime)
