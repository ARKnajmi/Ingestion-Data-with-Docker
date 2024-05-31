#!/usr/bin/env python
# coding: utf-8

import os
import argparse

import pandas as pd
from sqlalchemy import create_engine
from time import time

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    csv_name = f"output1.csv"
    
    
    os.system(f"wget {url} -O {csv_name}")
    
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")
    
    df_zones  = pd.read_csv(csv_name, index_col=[0]) 
    df_zones.to_sql(name="zones", con=engine, if_exists="replace")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Ingest Data CSV to Postgres')

    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host name for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='user name for postgres')
    parser.add_argument('--table_name', help='name of the table where we will write the results to')
    parser.add_argument('--url', help='url of the csv file')

    args = parser.parse_args()
    
    main(args)







