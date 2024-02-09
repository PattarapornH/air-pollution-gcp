# Air Pollution


The goal of this repository is to extract air quality data from [openweather](https://github.com/PattarapornH/air-pollution-airflow/blob/main/openweathermap.org). This project is built on the Google Cloud Platform. Cloud Scheduler releases messages to Cloud Pub/Sub, and Cloud Functions are activated accordingly. 
The air quality location is determined by the provincial office in the 77 provinces of Thailand. The geographical data is sourced from the [website](https://data.go.th/dataset/province-lat-long) of the Thai government.

Air quality data is visually presented using [Looker Studio](https://lookerstudio.google.com/u/0/reporting/3cfa03ef-82af-483d-89dd-9dc0c6fa2bd5/page/p_2nr4yrckdd), offering detailed insights on the latest air quality and its trend, aiding in understanding whether it is good or bad.


Disclaimer: This data may lack precision as it's based on the location of governor offices in each province, not capturing air quality in all areas. However, the overall trend still serves as an indicator of broader patterns.

