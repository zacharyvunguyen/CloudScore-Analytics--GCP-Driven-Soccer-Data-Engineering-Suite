# CloudScore Analytics: GCP-Driven Soccer Data Engineering Suite
![GCP project.png](img%2FGCP%20project.png)
## Introduction
Tableau Dashboard:
![Tableau Dashboard.png](img%2FTableau%20Dashboard.png)
"CloudScore Analytics: GCP-Driven Soccer Data Engineering Suite" is a sophisticated data engineering project that leverages Google Cloud Platform's robust capabilities for end-to-end management of soccer statistics.
Utilizing Python for data extraction from API Football, the suite introduces a meticulous data cleaning phase, ensuring the highest data quality and integrity. The project involves automated workflows for data processing and storage in GCP Cloud Storage. Employing Google Dataflow, the suite ensures streamlined data transfer to BigQuery tables. Key features include Cloud Function-triggered data transformation into BigQuery tables and insightful visualization using Tableau. Orchestrated daily by Cloud Composer, this project exemplifies state-of-the-art data pipeline automation and analytics in the cloud.

## Technologies Used

- Python
- Google Cloud Platform (GCP) components:
  - Cloud Storage
  - Cloud Functions
  - Dataflow
  - BigQuery
  - Cloud Composer
- Tableau for Visualization
- API Football for Data Source

## Features

- **Automated Data Extraction**: Seamlessly pull data from API Football.
- **GCP-Powered Transformation and Storage**: Leverage GCP services for efficient data handling.
- **Daily Orchestrated Data Pipeline Runs**: Ensure consistent data flow with Cloud Composer.
- **Interactive Tableau Visualizations**: Create dynamic visual representations of data.



## Setup and Installation
To get this project up and running, follow these steps:
1. Clone the repository:
   ```
   git clone [https://github.com/zacharyvunguyen/CloudScore-Analytics--GCP-Driven-Soccer-Data-Engineering-Suite.git]
   cd [CloudScore-Analytics--GCP-Driven-Soccer-Data-Engineering-Suite]
2. [Further steps regarding setting up GCP services, configuring API keys, etc.]

## Usage
This suite comprises several steps to automate soccer data management using GCP. Follow these steps to set up the entire workflow:

1. **Initialize Cloud Storage Bucket:**
   Execute the script to create a new bucket in Cloud Storage.
   ```bash
   python Create_Cloud_Storage_Bucket.py
   ```

2. **Data Extraction and Storage:**
   Run the script to fetch soccer data from API Football, perform data cleaning, and store the processed data in Cloud Storage.
   ```bash
   python Fetching_API_Data_to_CloudStorage.py
   ```

3. **BigQuery Dataset and Table Setup:**
   Create a BigQuery dataset and table using the following script.
   ```bash
   python Create_BigQuery_Dataset_and_Table_No_Schema.py
   ```

4. **Prepare Dataflow Metadata:**
   Set up the necessary parameters for Dataflow by running:
   ```bash
   python Prepare_Dataflow_Parameters.py
   ```

5. **Dataflow Job Execution:**
   - Configure and initiate a Dataflow job to move data from Cloud Storage to BigQuery.
     ![Dataflow_Setup.png](img%2FDataflow_Setup.png)
     ![Dataflow_Setup_1.png](img%2FDataflow_Setup_1.png)
   - View the results and job graph upon completion.
     ![Dataflow_JobGraph.png](img%2FDataflow_JobGraph.png)
     ![BigQuery_Succeeded_Load.png](img%2FBigQuery_Succeeded_Load.png)

6. **Automate Dataflow with Cloud Function:**
   Deploy a Cloud Function to trigger Dataflow jobs automatically when new files are uploaded to Cloud Storage.
   ![CloudFuntions_Setup_1.png](img%2FCloudFuntions_Setup_1.png)
   ![CloudFuntions_Setup_2.png](img%2FCloudFuntions_Setup_2.png)

7. **Orchestrate Data Pipeline with Cloud Composer:**
   - Set up the Cloud Composer environment to manage and schedule the data pipeline.
     ![CloudComposer_Setup_1.png](img%2FCloudComposer_Setup_1.png)
   - Upload the DAG file to Cloud Storage to automate the workflow.
     ```bash
     python Prepare_CloudCompoers_Files.py
     ```
     ![Cloud_Composer_DAGs.png](img%2FCloud_Composer_DAGs.png)

## Visualizations
BigQuery to Tableau Connection:
![Tableau_BigQuery.png](img%2FTableau_BigQuery.png)
Tableau Dashboard:
![Tableau Dashboard.png](img%2FTableau%20Dashboard.png)

