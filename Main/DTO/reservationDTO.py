from uuid import UUID
from pydantic import BaseModel, validator
from datetime import date
import re
from Modele.reservation import Reservation
from DTO.chambreDTO import ChambreDTO

class ReservationDTO(BaseModel):
    fk_id_client: UUID  # Client ID is mandatory
    fk_id_chambre: UUID  # Chambre ID is mandatory
    dateDebut: date  # Start date is mandatory
    dateFin: date  # End date is mandatory
    prixParJour: float  # Daily price is mandatory
    infoReservation: str | None = None  # Reservation info is optional
    chambre: ChambreDTO | None = None  # ChambreDTO (if needed)

    @validator("dateDebut", "dateFin", pre=True)
    def validate_dates(cls, value):
        if value is None:
            raise ValueError("Les dates sont requises.")
        if isinstance(value, str):
            # Validate the date format
            if not re.match(r"^\d{4}-\d{2}-\d{2}$", value):
                raise ValueError("La date doit être au format YYYY-MM-DD.")
            # Convert the string to a date object
            return date.fromisoformat(value)
        return value

    @validator("prixParJour")
    def prix_positif(cls, value):
        if value <= 0:
            raise ValueError("Le prix par jour doit être positif.")
        return value

    @classmethod
    def from_model(cls, reservation: Reservation):
        return cls(
            fk_id_client=reservation.fk_id_client,
            fk_id_chambre=reservation.fk_id_chambre,
            dateDebut=reservation.date_debut_reservation.date(),
            dateFin=reservation.date_fin_reservation.date(),
            prixParJour=reservation.prix_jour,
            infoReservation=reservation.info_reservation,
            chambre=ChambreDTO.from_model(reservation.chambre) if reservation.chambre else None, 
        )


class CriteresRechercheDTO(BaseModel):
    idReservation: str | None = None
    idClient: str | None = None
    idChambre: str | None = None
    nom: str | None = None
    prenom: str | None = None

    class Config:
        from_attributes = True
