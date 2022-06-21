import pandas as pd
from sqlalchemy import create_engine
import psycopg2
import sys

# Connection parameters
param_dic = {
    "host"      : "localhost",
    "database"  : "vidrio",
    # "user"      : "vid",
    "user"      : "albamolina",
    "password"  : "yourpassword"
}

def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1) 
    print("Connection successful")
    return conn

connect(param_dic)



