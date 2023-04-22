## SQL Server to MongoDB Migration - Azure Function

#### This Azure Function is designed to migrate data from a SQL Server database to a MongoDB database. The function connects to both databases, retrieves the table schema from SQL Server, and then transfers the data to the corresponding MongoDB collections. The function is implemented in Python and utilizes the pymongo, pyodbc, and pandas libraries.
Dependencies
    
    requirements.txt
    
How to use

    Set up the required environment variables:
        SQL_CONNECTION_STRING: Connection string for the SQL Server database (must be ODBC 17)
        MONGO_CONN: Connection string for the MongoDB database
        DATABASE_NAME: Name of the new database in MongoDB

    Deploy the Azure Function with the ss_to_mongo function.

    Trigger the function to start the data migration process.

Function Explanation

The ss_to_mongo function performs the following steps:

    Connects to the SQL Server database using the provided connection string and establishes a cursor.

    Connects to the MongoDB database using the provided connection string and selects the specified database.

    Retrieves a list of all tables in the SQL Server database.

    Iterates through each table and performs the following steps:
        Creates a new collection in MongoDB with the same name as the SQL Server table.
        Reads the data from the SQL Server table into a pandas DataFrame.
        Replaces any missing values with the string "Null".
        Converts the DataFrame to a list of dictionaries.
        Inserts the dictionaries into the MongoDB collection using a bulk write operation.

Error Handling and Logging

The function utilizes Python's logging module to log information, warnings, and errors. If an exception occurs during the migration process, the function will log the exception and terminate.
