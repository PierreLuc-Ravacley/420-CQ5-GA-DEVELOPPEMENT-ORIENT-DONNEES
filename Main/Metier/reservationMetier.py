from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select
from DTO.reservationDTO import ReservationDTO
from Modele.reservation import Reservation
from Modele.chambre import Chambre,Client
from fastapi import HTTPException
from uuid import UUID

engine = create_engine('mssql+pyodbc://DESKTOP-6KMCBC1\\SQLEXPRESS01/Hotel?driver=SQL Server', use_setinputsizes=False)

#Test que je recois bien les réservations
def get_reservations():
    with Session(engine) as session:
        stmt = select(Reservation)
        result = session.execute(stmt)
        reservations = result.scalars().all()
        return [ReservationDTO.from_model(reservation=r) for r in reservations]


def creer_reservation(reservation: ReservationDTO):
    with Session(engine) as session:
        # Vérifie si le client existe
        client = session.execute(select(Client).where(Client.id_client == reservation.fk_id_client)).scalar_one_or_none()
        if client is None:
            raise ValueError("Le client n'existe pas.")

        # Vérifie si la chambre existe et si elle est disponible
        chambre = session.execute(select(Chambre).where(Chambre.id_chambre == reservation.fk_id_chambre)).scalar_one_or_none()
        if chambre is None or not chambre.disponible_reservation:
            raise ValueError("La chambre n'existe pas ou n'est pas disponible.")

        # Validation des dates
        if reservation.dateDebut >= reservation.dateFin:
            raise ValueError("La date de début doit être antérieure à la date de fin.")

        # Vérifie que la chambre est libre pendant la période demandée
        stmt = select(Reservation).where(
            Reservation.fk_id_chambre == reservation.fk_id_chambre,
            Reservation.date_debut_reservation < reservation.dateFin,
            Reservation.date_fin_reservation > reservation.dateDebut
        )
        if session.execute(stmt).first() is not None:
            raise ValueError("La chambre est déjà réservée pendant cette période.")

        # Créer la réservation
        nouvelle_reservation = Reservation(
            fk_id_client=reservation.fk_id_client,
            fk_id_chambre=reservation.fk_id_chambre,
            date_debut_reservation=reservation.dateDebut,
            date_fin_reservation=reservation.dateFin,
            prix_jour=reservation.prixParJour,
            info_reservation=reservation.infoReservation
        )

        session.add(nouvelle_reservation)
        session.commit()

# Converti la réservation créée en dictionnaire avec from_orm
        reservation_dto = ReservationDTO.from_orm(nouvelle_reservation).dict()
        
        return reservation_dto
    

    
def supprimer_reservation(id_reservation: UUID):
    with Session(engine) as session:
        # Vérifie si la réservation existe
        reservation = session.execute(select(Reservation).where(Reservation.id_reservation == id_reservation)).scalar_one_or_none()
        if reservation is None:
            raise ValueError("La réservation n'existe pas.")

        # Supprime la réservation
        session.delete(reservation)
        session.commit()

        return {"status": "Réservation supprimée avec succès."}