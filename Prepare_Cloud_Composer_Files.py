from google.cloud import storage
import logging

def upload_file_to_gcs_bucket(bucket_name, source_file_path, destination_blob_name):
    """Uploads a file to the specified location in the GCS bucket."""
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_path)
        logging.info(f"Uploaded {source_file_path} to {destination_blob_name} in bucket {bucket_name}")
    except Exception as e:
        logging.error(f"Failed to upload {source_file_path} to {destination_blob_name}: {str(e)}")

def main():
    bucket_name = 'us-central1-daily-trigger-c-e9070abf-bucket'

    # Upload 'CloudComposer_DAG.py' to the 'dags' folder
    upload_file_to_gcs_bucket(bucket_name, 'CloudComposer_DAG.py', 'dags/CloudComposer_DAG.py')

    # Upload 'Fetching_API_Data_to_CloudStorage.py' to the 'scripts' folder within the 'dags' folder
    upload_file_to_gcs_bucket(bucket_name, 'Fetching_API_Data_to_CloudStorage.py', 'dags/scripts/Fetching_API_Data_to_CloudStorage.py')

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)  # Set the logging level to INFO
    main()
