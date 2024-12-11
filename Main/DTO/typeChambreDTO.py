from pydantic import BaseModel
from Modele.typeChambre import TypeChambre


# Data Transfer Object : pydantic BaseModel pour intégration facile avec FastAPI
class TypeChambreDTO(BaseModel):
    
    nom_type: str
    prix_plafond: float
    prix_plancher: float
    description_chambre : str

    def __init__(self, type: TypeChambre):
        super().__init__(nom_type="", prix_plafond=0.0, prix_plancher=0.0, description_chambre="")
        self.nom_type = type.nom_type
        self.prix_plafond = type.prix_plafond
        self.prix_plancher = type.prix_plancher
        self.description_chambre = type.description_chambre
        