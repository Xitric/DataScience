from sf_crime_mapper.api.sfgov_api_fetcher import ApiFetcher
from sf_crime_mapper.models.incident_report import IncidentReport


def handler(results):
    for res in results:
        print(res.incident_description)


if __name__ == "__main__":
    # spark = SparkSession.builder.master("local[*]").getOrCreate()
    # df = spark.read.csv("/work/DataScience/311_Cases.csv")
    # print(df.count())
    fetcher = ApiFetcher(IncidentReport)
    fetcher.get_new_data(IncidentReport.to_struct_time("2019-11-07T00:00:00.000"), handler)
