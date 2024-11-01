from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select
from Modele.chambre import Reservation, Client
from DTO.reservationDTO import CriteresRechercheDTO, ReservationDTO
engine = create_engine('mssql+pyodbc://localhost\\sqlexpress01/Hotel?driver=SQL Server', use_setinputsizes=False)

def rechercherReservation(criteres: CriteresRechercheDTO):
    with Session(engine) as session:

        if(criteres.prenom and not len(criteres.prenom) > 60):
            raise ValueError('Le prenom est trop long')
            
        if(criteres.nom and not len(criteres.nom) > 60):
            raise ValueError('Le nom est trop long')
        
        if(not criteres.nom and criteres.prenom):
            raise ValueError('La recherche par prénom seulement n''est pas supportée. Veuiller indiquer un nom et prénom.')
        
        if(criteres.idChambre and not len(criteres.idChambre) == 36):
            raise ValueError('idChambre doit contenir 36 caractères')
        
        if(criteres.idClient and not len(criteres.idClient) == 36):
            raise ValueError('idClient doit contenir 36 caractères')
        
        if(criteres.idReservation and not len(criteres.idReservation) == 36):
            raise ValueError('idReservation doit contenir 36 caractères')

        stmt = select(Reservation)

        if(criteres.idReservation):
            stmt = stmt.where(Reservation.id_reservation == criteres.idReservation)
        
        if(criteres.idChambre):
            stmt = stmt.where(Reservation.fk_id_chambre == criteres.idChambre)

        if(criteres.idClient):
            stmt = stmt.where(Reservation.fk_id_client == criteres.idClient)

        if(criteres.nom):
            stmt = stmt.join(Client).where(Client.nom == criteres.nom)
            if(criteres.prenom):
                 stmt.where(Client.prenom == criteres.prenom)

        """ TODO :  Ajouter critère(s) de recherche, joins et validations correspondantes, au besoin"""
    
        reservations = []
        for reservation in session.execute(stmt).scalars():
            reservations.append(ReservationDTO(reservation))

        return reservations
           
            
            