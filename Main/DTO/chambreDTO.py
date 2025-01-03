from pydantic import BaseModel
from Modele.chambre import Chambre

# Data Transfer Object : pydantic BaseModel pour intégration facile avec FastAPI
class CriteresRechercheDTO(BaseModel):
    numero_chambre: str | None = None 
    #disponible_reservation : str
    
class ChambreDTO(BaseModel): 
    numero_chambre: int
    disponible_reservation : bool
    autre_informations: str | None
    type_chambre: str


    @classmethod
    def from_model(cls, chambre: Chambre):
        return cls(
            numero_chambre=chambre.numero_chambre,
            disponible_reservation=chambre.disponible_reservation,
            autre_informations=chambre.autre_informations,
            type_chambre=chambre.type_chambre.nom_type
    )

"""     def __init__(self, chambre: Chambre):
        super().__init__(numero_chambre=0, disponible_reservation=False, autre_informations="", type_chambre="")
        self.numero_chambre = chambre.numero_chambre
        self.disponible_reservation = chambre.disponible_reservation
        self.autre_informations = chambre.autre_informations
        self.type_chambre = chambre.fk_type_chambre """