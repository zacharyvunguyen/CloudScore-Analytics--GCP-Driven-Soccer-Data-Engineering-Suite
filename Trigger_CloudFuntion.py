from googleapiclient.discovery import build
import logging

def trigger_dataflow_gcs_to_bigquery_job(cloud_event, environment):
    try:
        # Initialize Dataflow service
        service = build('dataflow', 'v1b3')
        project = "cloudscore20240120"
        template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

        # Job setup
        template_body = {
            "jobName": "dataflow-gcs-to-bigquery-job",
            "parameters": {
                "javascriptTextTransformGcsPath": "gs://cloudscore-dataflow-metadata/Dataflow_udf.js",
                "JSONPath": "gs://cloudscore-dataflow-metadata/Dataflow_BigQuery-Schema.json",
                "javascriptTextTransformFunctionName": "transform",
                "outputTable": "cloudscore20240120:premier_league.players_stats",
                "inputFilePattern": "gs://2024test/players_data.csv",
                "bigQueryLoadingTemporaryDirectory": "gs://cloudscore-dataflow-metadata",
            }
        }

        # Launch job
        request = service.projects().templates().launch(
            projectId=project,
            gcsPath=template_path,
            body=template_body
        )
        response = request.execute()
        logging.info("Dataflow job launched.")

    except Exception as e:
        logging.error(f"Job launch error: {e}")

