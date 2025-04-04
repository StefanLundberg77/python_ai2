import os
import requests
import dlt
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path

# testa utan om de funkar i name main
# working_directory = Path(__file__).parent
# os.chdir(working_directory)


# create a function to be used in the generator function
def get_data(base_url, params):
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

# use the dlt.resource decorator to produce a dlt.resource object
@dlt.resource(write_disposition="replace")

# define the generator function with yield keyword, to be decorated by dlt.resource decorator
def weather_data_resource():

    # load env
    load_dotenv()

    base_url = "https://api.openweathermap.org/data/2.5/weather"

    # cities list to request data from
    cities = ["Göteborg","Stockholm","London","Paris","New York", "Tokyo"]
    
    # get keys
    weather_api_key = os.getenv("WEATHER_API_KEY")

    # loop through list to get data for each city
    for city in cities:
        params = {
        "q": city,
        "appid": weather_api_key,
        "units": "metric"}
        data = get_data(base_url, params)
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

def run_pipeline():
    # create a dlt-pipeline
    pipeline = dlt.pipeline(pipeline_name="weather_pipeline",
                            destination=dlt.destinations.duckdb(f"{working_directory}/weather.duckdb"),
                            dataset_name="staging"  # detta blir "schema" i DuckDB
                            )
    load_info = pipeline.run(weather_data_resource(), table_name="weather_by_city")
    print(load_info)

if __name__=="__main__":
    #confirm the working directory is the one storing the .dlt folder, which is the same as the folder storing the current file
    working_directory = Path(__file__).parent
    os.chdir(working_directory)

    run_pipeline()

# # connect to db
#con = duckdb.connect("weather.duckdb")

# # view first rows
# result = con.execute("SELECT * FROM staging.weather_by_city").fetchdf()

# con.execute("SHOW TABLES FROM staging").fetchall()