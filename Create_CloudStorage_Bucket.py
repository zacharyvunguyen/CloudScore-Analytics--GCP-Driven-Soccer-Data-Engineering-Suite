from google.cloud import storage
from google.cloud.storage import Bucket

def create_bucket(bucket_name, project='cloudscore20240120', location='US'):
    """
    Creates a new bucket in Google Cloud Storage.

    Parameters:
    bucket_name (str): The name of the bucket to create.
    project (str, optional): The ID of the GCP project in which to create the bucket. If not set, defaults to the project set in the environment.
    location (str, optional): The location in which to create the bucket. Defaults to 'US'.

    Returns:
    Bucket: The created bucket.
    """
    storage_client = storage.Client(project=project)
    bucket = storage_client.bucket(bucket_name)
    new_bucket = storage_client.create_bucket(bucket, location=location)

    print(f"Bucket {new_bucket.name} created in {new_bucket.location} with storage class {new_bucket.storage_class}")
    return new_bucket

if __name__ == "__main__":
    bucket_name = input("Enter the name for the new bucket: ")
    # Optionally you can also input project and location
    create_bucket(bucket_name)
