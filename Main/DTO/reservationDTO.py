import datetime
from pydantic import BaseModel
from DTO.chambreDTO import ChambreDTO
from Modele.chambre import Reservation
from uuid import UUID

# Data Transfer Object : pydantic BaseModel pour intégration facile avec FastAPI
class CriteresRechercheDTO(BaseModel):
    idReservation: str
    idClient: str
    idChambre: str
    nom: str
    prenom: str

class ReservationDTO(BaseModel):
    idReservation: UUID
    dateDebut : datetime.datetime
    dateFin : datetime.datetime
    prixParJour : float
    infoReservation : str
    chambre : ChambreDTO
    """ TODO :client : ClientDTO """

    def __init__(self, reservation: Reservation):
         super().__init__(idReservation=reservation.id_reservation, 
                          dateDebut=reservation.date_debut_reservation, 
                          dateFin=reservation.date_fin_reservation, 
                          prixParJour=reservation.prix_jour, 
                          infoReservation = reservation.info_reservation,
                          chambre = ChambreDTO(reservation.chambre))
         """ TODO : client = ClientDTO(type.client) """

   