import logging

import azure.functions as func

import pyodbc
import pymongo
from database_migrator import ss_to_mongo


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    sqlcon = req.params.get('sqlcon')
    mongocon = req.params.get('mongocon')
    dbn = req.params.get('dbn')
    try:
        ss_to_mongo(sql_connection_string=sqlcon, mongo_conn=mongocon, database_name=dbn)
        return func.HttpResponse("Success.", status_code=200)
    except Exception as e:
        logging.error(e)

    # if name:
    #     return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #          status_code=200
    #     )
