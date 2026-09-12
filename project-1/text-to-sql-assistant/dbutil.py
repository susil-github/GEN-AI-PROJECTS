import pandas as pd

from sqlalchemy import create_engine
import pymysql


#table = "emp"

engine = create_engine(
    "mysql+pymysql://root:root@localhost:3306/susil_db"
)
# Create MySQL connection


# def get_connection(database):
#     connection = mysql.connector.connect(
#         host="localhost",
#         port=3306,
#         user="root",
#         password="root",
#         database=database
#     )
#     return connection

#Now execute Query


def execute_query(query):
    df = pd.read_sql(query, engine)
    return df


def get_schema(table):
    schema_query = f'''select
     table_name,
     column_name,
     data_type
     FROM information_schema.columns
     WHERE table_schema = 'susil_db'
     AND table_name = '{table}'
     ORDER BY ordinal_position;'''

    return execute_query(schema_query)


#query = f''' select * from {table}'''
#schema = get_schema(table)
#result = execute_query(query=query)
# print(f'the result is \n:{schema}')
