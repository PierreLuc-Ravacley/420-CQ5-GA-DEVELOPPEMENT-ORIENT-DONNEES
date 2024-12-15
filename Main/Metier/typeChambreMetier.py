from DTO.typeChambreDTO import TypeChambreDTO
from database import SessionLocal

def creerTypeChambre(typeChambre: TypeChambreDTO):
     with SessionLocal() as session:
        nouveauTypeChambre = typeChambre (typeChambre)

        session.add(nouveauTypeChambre)
        session.commit()
        
        return typeChambre