from google.cloud import bigquery
from google.api_core.exceptions import Conflict

# Define the project ID
project_id = "cloudscore20240120"
# Define the dataset ID
dataset_id = f"{project_id}.premier_league"
# Define the table ID
table_id = f"{dataset_id}.players_stats"

# Initialize a BigQuery client
with bigquery.Client() as client:
    # Define the dataset properties
    dataset = bigquery.Dataset(dataset_id)
    dataset.location = "US"  # Set the location to the US

    # Try to create the dataset
    try:
        client.create_dataset(dataset, timeout=30)  # Set a 30-second timeout
        print(f"Dataset {dataset_id} created.")
    except Conflict:
        print(f"Dataset {dataset_id} already exists.")

    # Define the table properties without a schema
    table = bigquery.Table(table_id)

    # Try to create the table
    try:
        client.create_table(table)
        print(f"Table {table_id} created in BigQuery.")
    except Conflict:
        print(f"Table {table_id} already exists.")
