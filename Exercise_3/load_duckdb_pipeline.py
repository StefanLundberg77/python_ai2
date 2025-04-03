from dotenv import load_dotenv
import os
import requests
from datetime import datetime
import dlt

# load env
load_dotenv()

# get keys
weather_api_key = os.getenv("WEATHER_API_KEY")
stockholm_api_key = os.getenv("STOCKHOLM_API_KEY")

# base url for api
weather_url = "https://api.openweathermap.org/data/2.5/weather"

# cities list to request data from
cities = ["Stockholm","London","Paris","New York", "Tokyo"]

# function for get data from api
def get_weather_data():
    for city in cities:
        params = {
            "q": city,
            "appid": weather_api_key,
            "units": "metric"
        }
        response = requests.get(weather_url, params=params)
        data = response.json()

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


# create a dlt-pipeline
pipeline = dlt.pipeline(
    pipeline_name="weather_pipeline",
    destination="duckdb",
    dataset_name="staging"  # detta blir "schema" i DuckDB
)

# run pipeline & write data to table
info = pipeline.run(get_weather_data(), table_name="weather_by_city", write_disposition="append")

