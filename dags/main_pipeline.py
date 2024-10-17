from airflow.providers.google.cloud.transfers.sftp_to_gcs import SFTPToGCSOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator

from airflow import DAG

default_args = {
        'owner' : 'omkarpatil-14',
        'schedule' : "0 6 * * *"
    }
with DAG(
    dag_id="clean_saas_billing_data",
    default_args=default_args,
) as dag:
    project_id = 'omkar_prod'
    file_name = 'dummy_saas_data.csv'
    sftp_path = f'/home/omkar-server/my-data/{file_name}'
    gcs_bucket = 'omkar_main_bucket'
    gcs_path = f'billing_data/{file_name}'


    extract_data_from_sftp = SFTPToGCSOperator(
        task_id="extract_data_from_sftp_to_gcs",
        sftp_conn_id = 'my_sftp_conn_id',
        source_path = sftp_path,
        destination_bucket = gcs_bucket,
        destination_path = gcs_path,
        dag=dag
    )

    load_data_to_bq = GCSToBigQueryOperator(
        task_id="load_data_gcs_to_bq",
        bucket = gcs_bucket,
        source_objects = gcs_path,
        destination_project_dataset_table = "omkar-prod.billing_dataset.saas_billing_data",
        write_disposition = 'WRITE_TRUNCATE',
        source_format="CSV",
        skip_leading_rows=1,
        dag=dag
    )

    clean_billing_data = BigQueryExecuteQueryOperator(
        task_id="clean_data_in_bq",
        sql="dags_sql/clean_billing_data.sql",
        use_legacy_sql=False
    )

    process_invalid_data = BigQueryExecuteQueryOperator(
        task_id="process_invalid_data_in_bq",
        sql="dags_sql/process_invalid_data.sql",
        use_legacy_sql=False
    )

    # Execution Flow
    extract_data_from_sftp >> load_data_to_bq >> clean_billing_data >> process_invalid_data

