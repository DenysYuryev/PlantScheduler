import pyodbc
from PyQt5 import QtWidgets

# SQL connection and data reading
SERVER_NAME = 'VM-SV101-TULCHI\PLANTIT'
DATABASE_NAME = 'dbIdc'
USERNAME = 'sa'
PASSWORD = 'ProAdmin777'


def SQLconnection():
    try:
        connection_string = f'DRIVER={{SQL Server}};' \
                            f'SERVER={SERVER_NAME};' \
                            f'UID={USERNAME};' \
                            f'PWD={PASSWORD};' \
                            f'DATABASE={DATABASE_NAME}'

        connection = pyodbc.connect(connection_string)
        return connection
    except Exception as Error:
        res = QtWidgets.QMessageBox.critical(f'Error', f"Read data from SQL error: {Error}.\n")
        if res == QtWidgets.QMessageBox.Ok:
            connection.close()
            return 0


def SQLread(table_name):
    SQL_STATEMENT = f"SELECT * FROM dbo.{table_name}"
    try:
        cursor = SQLconnection().cursor()
        cursor.execute(SQL_STATEMENT)

        for row in cursor:
            print(row)
    except Exception as Error:
        res = QtWidgets.QMessageBox.critical(f'Error', f"Read data from SQL error: {Error}.\n")
        if res == QtWidgets.QMessageBox.Ok:
            SQLconnection().close()
            return 0
