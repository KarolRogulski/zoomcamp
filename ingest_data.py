import pandas as pd
from sqlalchemy import create_engine
import pyarrow.parquet as pq
from time import time
import argparse
import os

def get_args():
    parser = argparse.ArgumentParser(description='Ingest CSV data into Postgres')
    parser.add_argument('--user', help='user name')
    parser.add_argument('--password', help='password')
    parser.add_argument('--host', help='host')
    parser.add_argument('--port', help='port')
    parser.add_argument('--db', help='database')
    parser.add_argument('--table_name', help='table name')
    parser.add_argument('--url', help='url')

    return parser.parse_args()

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    file_name = 'yellow_tripdata_2021-01.parquet'

    command = f'wget {url} -O {file_name}'
    print(command)
    os.system(command)

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    
    parquet_file = pq.ParquetFile(file_name)

    for batch in parquet_file.iter_batches():
        t_start = time()
        
        df = batch.to_pandas()
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
        
        df.to_sql(name=table_name, con=engine, if_exists='append')

        t_end = time()
        print('Time: %.3f second' % (t_end - t_start))

if __name__ == '__main__':
    args = get_args()
    main(args)