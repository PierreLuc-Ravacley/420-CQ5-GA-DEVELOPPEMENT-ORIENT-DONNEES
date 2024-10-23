from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select
from DTO.reservationDTO import ReservationDTO
from Modele.reservation import Reservation
from Modele.chambre import Chambre,Client

engine = create_engine('mssql+pyodbc://DESKTOP-6KMCBC1\\SQLEXPRESS01/Hotel?driver=SQL Server', use_setinputsizes=False)

def get_reservations():
    with Session(engine) as session:
        stmt = select(Reservation)
        result = session.execute(stmt)
        reservations = result.scalars().all()
        return [ReservationDTO.from_model(reservation=r) for r in reservations]


def creer_reservation(reservation: ReservationDTO):
    with Session(engine) as session:
        # Vérifier si le client existe
        client = session.execute(select(Client).where(Client.id_client == reservation.fk_id_client)).scalar_one_or_none()
        if client is None:
            raise ValueError("Le client n'existe pas.")

        # Vérifier si la chambre existe et si elle est disponible
        chambre = session.execute(select(Chambre).where(Chambre.id_chambre == reservation.fk_id_chambre)).scalar_one_or_none()
        if chambre is None or not chambre.disponible_reservation:
            raise ValueError("La chambre n'existe pas ou n'est pas disponible.")

        # Validation des dates
        if reservation.dateDebut >= reservation.dateFin:
            raise ValueError("La date de début doit être antérieure à la date de fin.")

        # Vérifier que la chambre est libre pendant la période demandée
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

        return ReservationDTO(nouvelle_reservation)