from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select
from DTO.typeChambreDTO import TypeChambreDTO
from Modele.chambre import TypeChambre

engine = create_engine('mssql+pyodbc://LAPTOP-PL76LM4V\SQLEXPRESS02/Hotel?driver=SQL Server', use_setinputsizes=False)

def creerTypeChambre(typeChambre: TypeChambreDTO):
     with Session(engine) as session:
        nouveauTypeChambre = typeChambre (typeChambre)

        session.add(nouveauTypeChambre)
        session.commit()
        
        return typeChambre