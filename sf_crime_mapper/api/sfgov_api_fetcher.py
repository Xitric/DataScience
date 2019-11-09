from sf_crime_mapper.models.api_object import ApiObject
from datetime import datetime
import requests
import os


class ApiFetcher:
    """Used for fetching new data from an endpoint on data.sfgov.org"""

    DOMAIN = "https://data.sfgov.org/resource/"
    URL_TEMPLATE = "{}{}.json?$where={}>'{}'"
    APP_TOKEN = os.environ['APP_TOKEN']

    def __init__(self, object_type):
        self.time_identifier = object_type.date_name()
        self.resource_identifier = object_type.RESOURCE_ID
        self.object_factory = object_type.from_dictionary

    def get_new_data(self, since, handler):
        while True:
            url = self.__create_url(since)
            response = requests.get(url, headers={"X-App-Token": self.APP_TOKEN})
            response_body = response.json()

            if len(response_body) == 0:
                break

            results = map(self.object_factory, response_body)
            handler(results)
            since = self.object_factory(response_body[-1]).date()

    def __create_url(self, timestamp):
        time_string = datetime.strftime(timestamp, ApiObject.TIME_FORMAT)
        return self.URL_TEMPLATE.format(self.DOMAIN,
                                        self.resource_identifier,
                                        self.time_identifier,
                                        time_string)
