from google.cloud import storage
from google.cloud.exceptions import Conflict

def create_bucket_and_upload_files(bucket_name, file_names, location="US", make_public=False):
    storage_client = storage.Client()

    # Check if the bucket already exists
    if storage_client.lookup_bucket(bucket_name) is not None:
        print(f"Bucket {bucket_name} already exists.")
        return

    try:
        # Create a new bucket with the specified location
        bucket = storage_client.create_bucket(bucket_name, location=location)
        print(f"Created bucket {bucket_name} in {location}.")

        # Upload files
        for file_name in file_names:
            blob = bucket.blob(file_name)
            blob.upload_from_filename(file_name)
            if make_public:
                blob.make_public()
            print(f"Uploaded {file_name} to {bucket_name}. Public Access: {make_public}")

    except Conflict:
        print(f"A bucket with the name {bucket_name} already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

#
new_bucket_name = 'cloudscore-dataflow-metadata'
file_names = ['Dataflow_BigQuery-Schema.json', 'Dataflow_udf.js']  # File names in the root directory
create_bucket_and_upload_files(new_bucket_name, file_names, location="US", make_public=True)
