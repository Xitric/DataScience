from sf_crime_mapper.models.point import Point
from sf_crime_mapper.models.api_object import ApiObject


class ServiceCase(ApiObject):
    """Representation of a 311 service case since 2008"""

    RESOURCE_ID = "vw6y-z8j6"

    def __init__(self, service_request_id, requested_datetime, closed_date, updated_datetime, status_description,
                 status_notes, agency_responsible, service_name, service_subtype, service_details, address, street,
                 supervisor_district, neighborhoods_sffind_boundaries, police_district, lat, long, point, source,
                 media_url):
        self.service_request_id = service_request_id
        self.requested_datetime = requested_datetime
        self.closed_date = closed_date
        self.updated_datetime = updated_datetime
        self.status_description = status_description
        self.status_notes = status_notes
        self.agency_responsible = agency_responsible
        self.service_name = service_name
        self.service_subtype = service_subtype
        self.service_details = service_details
        self.address = address
        self.street = street
        self.supervisor_district = supervisor_district
        self.neighborhoods_sffind_boundaries = neighborhoods_sffind_boundaries
        self.police_district = police_district
        self.lat = lat
        self.long = long
        self.point = point
        self.source = source
        self.media_url = media_url

    @classmethod
    def from_dictionary(cls, dictionary):
        return cls(dictionary.get("service_request_id"),
                   dictionary.get("requested_datetime"),
                   dictionary.get("closed_date"),
                   dictionary.get("updated_datetime"),
                   dictionary.get("status_description"),
                   dictionary.get("status_notes"),
                   dictionary.get("agency_responsible"),
                   dictionary.get("service_name"),
                   dictionary.get("service_subtype"),
                   dictionary.get("service_details"),
                   dictionary.get("address"),
                   dictionary.get("street"),
                   dictionary.get("supervisor_district"),
                   dictionary.get("neighborhoods_sffind_boundaries"),
                   dictionary.get("police_district"),
                   dictionary.get("lat"),
                   dictionary.get("long"),
                   Point.from_dictionary(dictionary.get("point", {})),
                   dictionary.get("source"),
                   dictionary.get("media_url", {}).get("url"))

    @staticmethod
    def date_name():
        return "updated_datetime"

    def date(self):
        return self.to_struct_time(self.updated_datetime)
