from sqlalchemy import create_engine
from sqlalchemy.sql import text
from urllib.parse import quote_plus

# Connection string with parameters directly (bypassing DSN)
connection_string = quote_plus("DRIVER={ODBC Driver 17 for SQL Server};"
                               "SERVER=DESKTOP-6H6E5UF\\SQLEXPRESS;"
                               "DATABASE=hotelDB;"
                               "Trusted_Connection=yes;")


engine = create_engine(f"mssql+pyodbc:///?odbc_connect={connection_string}")


try:
    # Test the connection by executing a simple query
    with engine.connect() as connection:
        # Query to select all data from the Chambre table
        result = connection.execute(text("SELECT * FROM Chambre"))
        
        # Fetch all rows and print them
        rows = result.fetchall()
        for row in rows:
            print(row)
    
    
    
    class Base(DeclarativeBase):
        pass
        
        
        
     
    class Client(Base):
        __tablename__ = "Client"
        
    class Reservation(Base):
        __tablename__ = "chambre"
        
        
        
        
        
    
    class Chambre(Base):
        __tablename__ = "chambre"

        numero_chambre: Mapped[int]
        disponible_reservation: Mapped[bool]
        autre_informations: Mapped[str]
        id_chambre: Mapped[str] = mapped_column(primary_key=True)
        fk_type_chambre: Mapped[str] = mapped_column(ForeignKey("type_chambre.id_type_chambre"))

        type_chambre: Mapped['TypeChambre'] = relationship()


    class TypeChambre(Base):
        __tablename__ = "type_chambre"

        nom_type: Mapped[str]
        prix_plafond: Mapped[float]
        prix_plancher: Mapped[float]
        description_chambre: Mapped[str]
        id_type_chambre: Mapped[str] = mapped_column(primary_key=True)

        chambres: Mapped[List["Chambre"]] = relationship(back_populates="type_chambre")


except Exception as e:
    print(f"Error connecting to the database: {e}")