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

    base_url = "https://api.openweathermap.org/data/2.5/weather"

    # cities list to request data from
    cities = ["Göteborg","Stockholm","London","Paris","New York", "Tokyo"]
    
    # get keys
    weather_api_key = os.getenv("WEATHER_API_KEY") 

    for city in self.cities:
        params = {
            "q": city,
            "appid": weather_api_key,
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
# funct for requests
def get_request(base_url, params=None):
    response = requests.get(base_url, params=params)
    return response.json

# use the dlt.resource decorator to produce a dlt.resource object
@dlt.resource(write_disposition="replace")

# define the generator function with yield keyword, to be decorated by dlt.resource decorator
def data_resource(params):

    # loop through list to get data for each param
    for param in params:
        get_params()
        get_data()
        return params()

def run_pipeline(table_name,duckdb_name):
    # create a dlt-pipeline
    pipeline = dlt.pipeline(pipeline_name="weather_pipeline",
                            destination=dlt.destinations.duckdb(f"{working_directory}/{duckdb_name}"),
                            dataset_name="staging"  # detta blir "schema" i DuckDB
                            )

    load_info = pipeline.run(data_resource(), table_name=table_name)
    print(load_info)

if __name__=="__main__":
    #confirm the working directory is the one storing the .dlt folder, which is the same as the folder storing the current file
    working_directory = Path(__file__).parent
    os.chdir(working_directory)

    run_pipeline(table_name=)

