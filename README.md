# CloudScore Analytics: GCP-Driven Soccer Data Engineering Suite

## Introduction

"CloudScore Analytics: GCP-Driven Soccer Data Engineering Suite" is a sophisticated data engineering project that leverages Google Cloud Platform's robust capabilities for end-to-end management of soccer statistics. 
Utilizing Python for data extraction from API Football, the suite introduces a meticulous data cleaning phase, ensuring the highest data quality and integrity. The project involves automated workflows for data processing and storage in GCP Cloud Storage. Employing Google Dataflow, the suite ensures streamlined data transfer to BigQuery tables. Key features include Cloud Function-triggered data transformation into BigQuery tables and insightful visualization using Tableau. Orchestrated daily by Cloud Composer, this project exemplifies state-of-the-art data pipeline automation and analytics in the cloud.

## Technologies Used
- Python
- Google Cloud Platform (Cloud Storage, Cloud Functions, Dataflow, BigQuery, Cloud Composer)
- Tableau for Visualization
- API Football for Data Source

## Features
- Automated data extraction from API Football
- Data transformation and storage using GCP services
- Daily orchestrated data pipeline runs
- Interactive data visualizations in Tableau

## Setup and Installation
To get this project up and running, follow these steps:
1. Clone the repository:
   ```
   git clone [your-repo-link]
   cd [repository-name]
   ```
2. Install required Python packages:
   ```
   pip install -r requirements.txt
   ```
3. [Further steps regarding setting up GCP services, configuring API keys, etc.]

## Usage
1. Run the Python script to create a Cloud Storage bucket:
   ```
   python Create_Cloud_Storage_Bucket.py
   ```
2. Run the Python script to fetch the data from API Football, clean it, and store it in Cloud Storage buck:
   ```
   python Fetching_API_Data_to_CloudStorage.py
   ```
3. Run the Python script to create BigQuery dataset and table
   ```
   python Create_BigQuery_Dataset_and_Table_No_Schema.py
   ```
4. Run the Python script to create new bucket for dataflow metadata
   ```
   python Prepare_Dataflow_Parameters.py
   ```
5. Create & Run Dataflow Job to moves data from Cloud Storage to BigQuery 
   1. Set up Dataflow job with parameters
   ![Dataflow_Setup.png](img%2FDataflow_Setup.png)
   ![Dataflow_Setup_1.png](img%2FDataflow_Setup_1.png)
   2. Results
   ![Dataflow_JobGraph.png](img%2FDataflow_JobGraph.png)
   ![BigQuery_Succeeded_Load.png](img%2FBigQuery_Succeeded_Load.png)
6. Create and Deploy a Google Cloud Function to Automatically Initiate a Dataflow Job upon Detecting New File Uploads to Google Cloud Storage 
   1. ![CloudFuntions_Setup_1.png](img%2FCloudFuntions_Setup_1.png)
   2. ![CloudFuntions_Setup_2.png](img%2FCloudFuntions_Setup_2.png)
## Visualizations
Here are some examples of the visualizations created using Tableau:
![Visualization Example](link-to-image)

## Contributions and Feedback
Contributions to this project are welcome! Feel free to fork the repository and submit pull requests. For any feedback or issues, please open an issue in the repository.

## License
This project is licensed under the [MIT License](LICENSE.md).

## Contact
For any queries, feel free to contact me at [your-email@example.com].
