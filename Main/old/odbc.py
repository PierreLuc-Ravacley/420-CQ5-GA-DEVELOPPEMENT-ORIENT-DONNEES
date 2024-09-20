import pyodbc

# List all available ODBC drivers on the system
drivers = pyodbc.drivers()
print("Available ODBC drivers:")
for driver in drivers:
    print(driver)
