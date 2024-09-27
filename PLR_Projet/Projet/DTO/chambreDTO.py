from pydantic import BaseModel
from modele.chambre import TypeChambre, Chambre

# Data Transfer Object : pydantic BaseModel pour intégration facile avec FastAPI
class TypeChambreDTO(BaseModel):
    
    nom_type: str
    prix_plafond: float
    prix_plancher: float
    description_chambre : str

    def __init__(self, type: TypeChambre):
        self.nom_type = type.nom_type
        self.prix_plafond = type.prix_plafond
        self.prix_plancher = type.prix_plancher
        self.description_chambre = type.description_chambre

class ChambreDTO(BaseModel): 
    numero_chambre: int
    disponible_reservation : bool
    autre_informations: str
    type_chambre: str

    def __init__(self, chambre: Chambre):
        self.numero_chambre = chambre.numero_chambre
        self.disponible_reservation = chambre.disponible_reservation
        self.autre_informations = chambre.autre_informations
        self.type_chambre = chambre.type_chambre