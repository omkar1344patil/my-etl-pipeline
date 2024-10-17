# ELT Data Pipeline with Airflow and Google Cloud

This project is all about setting up an end-to-end ELT (Extract, Load, Transform) pipeline using Airflow and Google Cloud services. I wrote a detailed article about it on Medium, so if you're looking for the full explanation of how things work, you can check that out [here](https://medium.com/@omkar1344patil/building-an-end-to-end-etl-data-pipeline-with-airflow-and-google-cloud-ff9179edcf16).

### What's Happening Here?
- Data Ingestion: We pull data from a source and store it in Google Cloud Storage.
- Data Transformation: The raw data gets transformed using SQL.
- Loading into BigQuery: After cleaning up the data, it gets sent to BigQuery for analysis.
- Orchestration: Everything is scheduled and managed using Airflow, so it's automated and repeatable.


### Tools and Tech
- Airflow: Orchestration and scheduling
- Google Cloud Storage: For keeping our raw data
- BigQuery: Where the cleaned-up data ends up
- Python & SQL: For scripting and transforming data

### Prerequisites
To run this project, you'll need:

- Google Cloud Platform account with access to Cloud Storage and BigQuery
- Apache Airflow set up locally or on a server
- Python 3.7+ environment

### How to Run It?
Clone this repository:

``` git clone https://github.com/yourusername/your-repo-name.git```

### Set up your environment:
Make sure you have Airflow running locally, and your Google Cloud credentials set up to access Cloud Storage and BigQuery.
Place your Airflow DAGs in the right folder, update the configs (like your GCP project ID), and you're good to go!
Trigger the DAG manually in the Airflow UI or let it run based on the schedule.

### More Info
If you want more details on how this all comes together, including setup steps and code breakdowns, check out my full article on Medium: 
Read the article [here](https://medium.com/@omkar1344patil/building-an-end-to-end-etl-data-pipeline-with-airflow-and-google-cloud-ff9179edcf16).

### License
Feel free to use this project however you want—licensed under MIT.


