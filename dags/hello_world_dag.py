from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# DAG'ınızın varsayılan argümanlarını tanımlayın
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email': ['your_email@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# DAG tanımınızı oluşturun
dag = DAG(
    'hello_world',                # DAG'ınızın ismi
    default_args=default_args,
    description='A simple hello world DAG',
    # Her gün bir kere çalışacak şekilde zamanlayın
    schedule_interval=timedelta(days=1),
)

# Çalıştırılacak Python fonksiyonunu tanımlayın
def print_hello():
    return 'Hello World'

# PythonOperator kullanarak task oluşturun
hello_operator = PythonOperator(
    task_id='hello_task',         # Task'ınızın ismi
    python_callable=print_hello,  # Çağrılacak fonksiyon
    dag=dag,                      # Yukarıda tanımlanan DAG
)

# DAG'ınızı ve task'ınızı çalıştırmak için gerekli yapılandırmayı tamamladınız
