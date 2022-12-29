import pymongo
import pyodbc
import pandas as pd
import logging
import time

start_time = time.time()


def ss_to_mongo(sql_connection_string, mongo_conn, database_name):
    try:
    
        conn = pyodbc.connect(sql_connection_string)
        cursor = conn.cursor()

        logging.info('Connection to SQL Server Successful...')

        myclient = pymongo.MongoClient(mongo_conn)
        mydb = myclient[f"{database_name}"]

        logging.info('Connection to MongoDB Successful...')

        cursor.execute("SELECT '[' + TABLE_SCHEMA + '].[' + TABLE_NAME + ']' as tables FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
        tables = [table[0] for table in cursor.fetchall()]

        logging.info(f"Tables: {tables}")

        print(tables)

        for table in tables:
            mycol = mydb[table]
            sql = f"SELECT * FROM {table}"
            df = pd.read_sql(sql, conn)
            df.fillna('Null', inplace=True)
            records = df.to_dict(orient='records')
            if records:
                requests = [pymongo.InsertOne(record) for record in records]
                mycol.bulk_write(requests)
    except Exception as e:
        logging.exception(e)