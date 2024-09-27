from pydantic import BaseModel
from Modele.chambre import TypeChambre, Chambre,Client,Reservation
from uuid import UUID
from datetime import datetime 


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


#Data Transfer Object : pydantic BaseModel pour intégration facile avec FastAPI ajout de 
# ClientDTO et ReservationDT0

class ClientDTO(BaseModel):
    prenom: str
    nom: str
    adresse: str
    mobile: str
    mot_de_passe: str

    def __init__(self, client: Client):
        self.prenom = client.prenom
        self.nom = client.nom
        self.adresse = client.adresse
        self.mobile = client.mobile
        self.mot_de_passe = client.mot_de_passe

class ReservationDTO(BaseModel):
    date_fin_reservation: datetime
    date_debut_reservation: datetime
    prix_jour: float
    info_reservation: str
    fk_id_client: UUID
    fk_id_chambre: UUID

    def __init__(self, reservation: Reservation):
        self.date_fin_reservation = reservation.date_fin_reservation
        self.date_debut_reservation = reservation.date_debut_reservation
        self.prix_jour = reservation.prix_jour
        self.info_reservation = reservation.info_reservation
        self.fk_id_client = reservation.fk_id_client
        self.fk_id_chambre = reservation.fk_id_chambre