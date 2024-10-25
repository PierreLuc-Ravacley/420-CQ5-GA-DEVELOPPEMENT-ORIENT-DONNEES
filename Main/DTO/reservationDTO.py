from pydantic import BaseModel, validator
from Modele.reservation import Reservation
from uuid import UUID
import datetime

# Data Transfer Object : pydantic BaseModel pour intégration facile avec FastAPI
class ReservationDTO(BaseModel):
    fk_id_client: UUID  # Client est obligatoire
    fk_id_chambre: UUID  # Chambre est obligatoire
    dateDebut: datetime.datetime  # Date de début est obligatoire
    dateFin: datetime.datetime  # Date de fin est obligatoire
    prixParJour: float  # Prix par jour est obligatoire
    infoReservation: str = None  # Info réservation est optionnel

    @validator('dateDebut', 'dateFin', pre=True)
    def validate_dates(cls, value):
        if value is None:
            raise ValueError('Les dates sont requises.')
        return value

    @validator('prixParJour')
    def prix_positif(cls, value):
        if value <= 0:
            raise ValueError('Le prix par jour doit être positif.')
        return value
     
    @classmethod
    def from_model(cls, reservation: Reservation):
        return cls(
            fk_id_client=reservation.fk_id_client,
            fk_id_chambre=reservation.fk_id_chambre,
            dateDebut=reservation.date_debut_reservation,
            dateFin=reservation.date_fin_reservation,
            prixParJour=reservation.prix_jour,
            infoReservation=reservation.info_reservation
        )
    
    class Config:
        orm_mode = True
       
