from sqlalchemy import select
from DTO.chambreDTO import ChambreDTO, CriteresRechercheDTO
from Modele.chambre import Chambre
from database import SessionLocal

def creerChambre(chambre: ChambreDTO):
    with SessionLocal() as session:
            stmt = select(typeChambre).where(typeChambre.nom_type == chambre.type_chambre)
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

def getChambreParNumero(no_chambre: int):
     with SessionLocal() as session:
        stmt = select(Chambre).where(Chambre.numero_chambre == no_chambre)
        result = session.execute(stmt)
        
        for chambre in result.scalars():
            return ChambreDTO (chambre)
        

def rechercherChambreLibre(criteres: CriteresRechercheDTO):
    with SessionLocal() as session:

        if(criteres.numero_chambre and not criteres.numero_chambre.isnumeric() == False):
            raise ValueError('Le numero de chambre doit être un numero')

        stmt = select(Chambre)

        #if(criteres.numero_chambre): 
         #   stmt = stmt.where(Chambre.numero_chambre == criteres.numero_chambre and Chambre.disponible_reservation == True)

        print(Chambre.disponible_reservation)
        """ TODO :  Ajouter critère(s) de recherche, joins et validations correspondantes, au besoin"""
    
        chambres = []
        for chambre in session.execute(stmt).scalars():
            if stmt.where(Chambre.numero_chambre == criteres.numero_chambre and Chambre.disponible_reservation == "1"):
                chambres.append(ChambreDTO(chambre))
        return  
           
            
            