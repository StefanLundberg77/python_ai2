import os
import requests
import dlt
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path

# load env for api keys
load_dotenv()

# create class for weather api data
class Weather_api:
        def __init__(self, api_key, base_url, cities):
            self.api_key = api_key
            self.base_url = base_url
            self.cities = cities

        # create function to store params
        def get_weather_data(self):

            for city in self.cities:
                params = {
                    "q": city,
                    "appid": self.api_key,
                    "units": "metric"}
                data = get_request(self.base_url, params)

                # return requested data
                yield {
                    "city": city,
                    "timestamp": datetime.now().isoformat(),
                    "temperature": data["main"]["temp"],
                    "humidity": data["main"]["humidity"],
                    "pressure": data["main"]["pressure"],
                    "weather_description": data["weather"][0]["description"],
                    "wind_speed": data["wind"]["speed"],
                    "cloudiness": data["clouds"]["all"]
                }
class Parking_api:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def get_parking_data(self):
        params = {
            "outputFormat": "json",
            "apiKey": self.api_key
        }
        data = get_request(self.base_url, params=params)

        for feature in data.get("features", []):
            properties = feature.get("properties", {})
            yield {
                "timestamp": datetime.now().isoformat(),
                "address": properties.get("ADRESS"),
                "city_district": properties.get("CITY_DISTRICT"),
                "parking_price": properties.get("PARKING_RATE", "Ej angiven")
            }
            # test to check json 
            print(data["features"][0])
            exit()
# resources to get
# timestamp
# address
# city district
# parking price
# funct for requests

# request function with responce status check
def get_request(base_url, params=None):
    response = requests.get(base_url, params=params)
    response.raise_for_status() #https://3.python-requests.org/user/quickstart/
    return response.json()

# dlt.resource decorator to produce a dlt.resource object
@dlt.resource(write_disposition="replace")

# define the generator function with yield keyword, to be decorated by dlt.resource decorator
def weather_data_resource(api:Weather_api):
    yield from api.get_weather_data()

def parking_data_resource(api:Parking_api):
    yield from api.get_parking_data()

# create source for adding and running another resource
@dlt.source

# sources for both resources returning data
def weather_source():

    weather_api = Weather_api(
        api_key=os.getenv("WEATHER_API_KEY"),
        base_url="https://api.openweathermap.org/data/2.5/weather",
        cities=["Göteborg","Stockholm","London","Paris","New York", "Tokyo"]       
    )
    return weather_data_resource(weather_api)

def parking_source():

    parking_api = Parking_api(
        api_key=os.getenv("STOCKHOLM_API_KEY"),
        base_url="https://openparking.stockholm.se/LTF-Tolken/v1/servicedagar/weekday/måndag"
        ) #/{WEEKDAY}?maxFeatures={MAXFEATURES}&outputFormat={FORMAT}&callback={CALLBACK}&apiKey={APIKEY}
    return parking_data_resource(parking_api)

# run function for pipeline
def run_pipeline(source, duckdb_name, table_name):
    # create a dlt-pipeline
    pipeline = dlt.pipeline(pipeline_name=table_name + "_pipeline",
                            destination=dlt.destinations.duckdb(os.path.join(working_directory, duckdb_name)),# trying without strformat
                            #destination=dlt.destinations.duckdb(f"{working_directory}/(duckdb_name)"),
                            dataset_name="staging"
                            )
    
    load_info = pipeline.run(source,table_name=table_name)
    # print message for test
    print(f"loaded {table_name} to {duckdb_name}")
    print(load_info)

if __name__=="__main__":
    #confirm the working directory is the one storing the .dlt folder, which is the same as the folder storing the current file
    working_directory = Path(__file__).parent
    os.chdir(working_directory)

    run_pipeline(
        source=weather_source(),
        duckdb_name="weather.duckdb",
        table_name="weather_by_city"
    )

    run_pipeline(
        source=parking_source(),
        duckdb_name="stockholm_parking.duckdb",
        table_name="parking_addresses"
    )