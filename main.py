import base64
from datetime import datetime
import logging
import time

import pandas as pd
import requests

from utils import write_dataframe_to_bq
from config import AIR_POLLUTION_API_KEY, GCP_PROJECT, BQ_DATASET, TABLE_NAME

URL = "https://api.openweathermap.org/data/2.5/air_pollution"


def get_pubsub_message(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event["data"]).decode("utf-8")
    return pubsub_message


def get_air_quality(lat, long):

    res = requests.get(
        url=URL, params={"lat": lat, "lon": long, "appid": AIR_POLLUTION_API_KEY}
    )
    
    return res


def main(event, context):
    messages = get_pubsub_message(event, context)

    if messages == "Daily getting air quality":
        pass
    else:
        raise Exception(f"`{messages}` messages does not support")


    coord = pd.read_parquet("./data/province_lat_long.parquet")

    air_qt_records = []
    for _, row in coord.iterrows():
        record = {"province": row["PROVINCE_NAME"]}

        res = get_air_quality(lat=row["LAT"], long=row["LNG"])
        print("{prov}: {code}".format(prov=row["PROVINCE_NAME"], code=res.status_code))
       
        air_qt = res.json()

        record.update(air_qt["list"][0]["main"])
        record.update(air_qt["list"][0]["components"])

        air_qt_records.append(record)

        # Free API
        time.sleep(2)

    air_qt_df = pd.DataFrame(air_qt_records)
    air_qt_df["updated_date"] = datetime.now().date()

    write_dataframe_to_bq(
        dataframe=air_qt_df,
        table_name=TABLE_NAME,
        dataset=BQ_DATASET,
        project_name=GCP_PROJECT,
    )

    print("DONE !")
