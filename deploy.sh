echo "Deploy to project $GCP_PROJECT" 
echo "Deploy to region $GCP_FUNCTION_REGION"
echo "Triggered by $GCP_TOPIC_AIR_POLLUTION topic"
echo "BQ dataset name $AIR_POLLUTION_BQ_DATASET"
echo "BQ table name $BQ_AIR_POLLUTION_TABLE_NAME"


gcloud functions deploy air-pollution-scraper \
    --entry-point main \
    --source . \
    --project $GCP_PROJECT \
    --runtime python39\
    --region $GCP_FUNCTION_REGION \
    --trigger-topic $GCP_TOPIC_AIR_POLLUTION  \
    --memory 1GB \
    --max-instances 1 \
    --set-env-vars="GCP_PROJECT"=$GCP_PROJECT \
    --set-env-vars="AIR_POLLUTION_BQ_DATASET"=$AIR_POLLUTION_BQ_DATASET \
    --set-env-vars="BQ_AIR_POLLUTION_TABLE_NAME"=$BQ_AIR_POLLUTION_TABLE_NAME \
    --set-env-vars="AIR_POLLUTION_API_KEY"=$AIR_POLLUTION_API_KEY \
    --timeout 540s