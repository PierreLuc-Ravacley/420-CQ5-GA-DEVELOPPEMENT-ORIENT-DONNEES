from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from DTO.typeChambreDTO import TypeChambreDTO

engine = create_engine('mssql+pyodbc://DESKTOP-6H6E5UF\\SQLEXPRESS/Hotel?driver=SQL Server', use_setinputsizes=False)

def creerTypeChambre(typeChambre: TypeChambreDTO):
     with Session(engine) as session:
        nouveauTypeChambre = typeChambre (typeChambre)

        session.add(nouveauTypeChambre)
        session.commit()
        
        return typeChambre