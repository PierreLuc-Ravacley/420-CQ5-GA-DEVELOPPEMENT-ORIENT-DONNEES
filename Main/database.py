from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the database URL (update this if your connection details change)
DATABASE_URL = 'mssql+pyodbc://DESKTOP-6H6E5UF\\SQLEXPRESS/Hotel?driver=SQL Server'

# Create the engine for the database connection
engine = create_engine(DATABASE_URL, use_setinputsizes=False)

# Create a sessionmaker to handle sessions for database interactions
SessionLocal = sessionmaker(bind=engine)