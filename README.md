# Air Pollution


The goal of this repository is to extract air quality data from [openweather](https://github.com/PattarapornH/air-pollution-airflow/blob/main/openweathermap.org). This project is built on the Google Cloud Platform. Cloud Scheduler releases messages to Cloud Pub/Sub, and Cloud Functions are activated accordingly. 
The air quality location is determined by the provincial office in the 77 provinces of Thailand. The geographical data is sourced from the [website](https://data.go.th/dataset/province-lat-long) of the Thai government.

