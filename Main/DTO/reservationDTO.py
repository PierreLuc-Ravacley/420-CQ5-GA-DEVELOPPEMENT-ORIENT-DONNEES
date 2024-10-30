from pydantic import BaseModel, validator
from Modele.reservation import Reservation
from uuid import UUID
from datetime import date
import re 

# Data Transfer Object : pydantic BaseModel pour intégration facile avec FastAPI
class ReservationDTO(BaseModel):
    fk_id_client: UUID  # Client est obligatoire
    fk_id_chambre: UUID  # Chambre est obligatoire
    dateDebut: date  # Date de début est obligatoire
    dateFin: date  # Date de fin est obligatoire
    prixParJour: float  # Prix par jour est obligatoire
    infoReservation: str = None  # Info réservation est optionnel

    @validator('dateDebut', 'dateFin', pre=True)
    def validate_dates(cls, value):
        if value is None:
            raise ValueError('Les dates sont requises.')
        if isinstance(value, str):
            # Vérifie le format de la date
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', value):
                raise ValueError('La date doit être au format YYYY-MM-DD.')
            # Convertir la chaîne en objet date
            return date.fromisoformat(value)
        return value

    @validator('prixParJour')
    def prix_positif(cls, value):
        if value <= 0:
            raise ValueError('Le prix par jour doit être positif. Exemple de 0 au maximum permis.')
        return value

    @classmethod
    def from_model(cls, reservation: Reservation):
        return cls(
            
            fk_id_client=reservation.fk_id_client,
            fk_id_chambre=reservation.fk_id_chambre,
            dateDebut=reservation.date_debut_reservation.date(),
            dateFin=reservation.date_fin_reservation.date(), 
            prixParJour=reservation.prix_jour,
            infoReservation=reservation.info_reservation
        )

class CriteresRechercheDTO(BaseModel):
    idReservation: str = None
    idClient: str = None
    idChambre: str = None
    nom: str = None
    prenom: str = None

    class Config:
       # orm_mode = True
        from_attributes = True 