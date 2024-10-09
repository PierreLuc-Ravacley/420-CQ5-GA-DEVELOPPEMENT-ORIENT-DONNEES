from pydantic import BaseModel
from Modele.reservation import Reservation
from datetime import datetime

# Data Transfer Object : pydantic BaseModel pour intégration facile avec FastAPI
class ReservationDTO(BaseModel):
    id_reservation: str
    date_debut_reservation: datetime
    date_fin_reservation: datetime
    prix_jour: float
    info_reservation: str
    fk_id_client: str
    fk_id_chambre: str

    def __init__(self, reservation:Reservation):
        super().__init__(id_reservation="", date_debut_reservation=datetime.min, date_fin_reservation=datetime.min, prix_jour=0.0, info_reservation="", fk_id_client="", fk_id_chambre="")
        self.id_reservation = reservation.id_reservation
        self.date_debut_reservation = reservation.date_debut_reservation
        self.date_fin_reservation = reservation.date_fin_reservation
        self.prix_jour = reservation.prix_jour
        self.info_reservation = reservation.info_reservation
        self.fk_id_client = reservation.fk_id_client
        self.fk_id_chambre = reservation.fk_id_chambre