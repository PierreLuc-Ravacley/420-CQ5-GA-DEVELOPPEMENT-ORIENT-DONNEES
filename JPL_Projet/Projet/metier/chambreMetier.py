
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select
from DTO.chambreDTO import ChambreDTO, TypeChambreDTO
from Modele.chambre import Chambre, TypeChambre

engine = create_engine('mssql+pyodbc://localhost\\sqlexpress01/Hotel?driver=SQL Server', use_setinputsizes=False)

def creerChambre(chambre: ChambreDTO):
    with Session(engine) as session:
            stmt = select(TypeChambre).where(TypeChambre.nom_type == chambre.type_chambre)
            result = session.execute(stmt)

            for typeChambre in result.scalars():
                
                nouvelleChambre = Chambre (
                    numero_chambre = chambre.numero_chambre,
                    disponible_reservation = chambre.disponible_reservation,
                    autre_informations = chambre.autre_informations,
                    type_chambre = typeChambre
                )

                session.add(nouvelleChambre)
                session.commit()
            
                return chambre
            
def creerTypeChambre(typeChambre: TypeChambreDTO):
     with Session(engine) as session:
        nouveauTypeChambre = TypeChambre (typeChambre)

        session.add(nouveauTypeChambre)
        session.commit()
        
        return typeChambre

def getChambreParNumero(no_chambre: int):
     with Session(engine) as session:
        stmt = select(Chambre).where(Chambre.numero_chambre == no_chambre)
        result = session.execute(stmt)
        
        for chambre in result.scalars():
            return ChambreDTO (chambre)