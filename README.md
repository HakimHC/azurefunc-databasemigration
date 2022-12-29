# Azure Function SQL Server to Mongo DB

This function migrates all of the data of a given SQL Server Database and migrates it to a new MongoDB database using PyODBC.
* Trigger type: HTTP 
* Parameters: sqlcon, mongocon, dbn 

* sqlcon -> SQL Server Connection String (DRIVER MUST BE ODBC DRIVER 17)
* mongocon -> MongoDB Connection String (Make sure you allow access from all networks in order for it to work)
* dbn -> Name of the new database to be created on MongoDB (Not your SQL Server database)

This is my first Azure Function.
