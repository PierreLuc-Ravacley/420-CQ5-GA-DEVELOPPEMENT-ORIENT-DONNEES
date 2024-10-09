from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select
from DTO.chambreDTO import ReservationDTO
from Modele.chambre import Reservation

engine = create_engine('mssql+pyodbc://DESKTOP-6KMCBC1\\SQLEXPRESS01/Hotel?driver=SQL Server', use_setinputsizes=False), use_setinputsizes=False)

def get_reservations():
    with Session(engine) as session:
        stmt = select(Reservation)
        result = session.execute(stmt)
        reservations = result.scalars().all()
        return [{"id": r.id_reservation, "date_debut": r.date_debut_reservation, "date_fin": r.date_fin_reservation} for r in reservations]

def creer_reservation(reservation: ReservationDTO):
    with Session(engine) as session:
        new_reservation = Reservation(
            date_debut_reservation=reservation.date_debut_reservation,
            date_fin_reservation=reservation.date_fin_reservation,
            prix_jour=reservation.prix_jour,
            info_reservation=reservation.info_reservation,
            client_id=reservation.fk_id_client,
            chambre_id=reservation.fk_id_chambre
        )
        session.add(new_reservation)
        session.commit()
        return {"message": "La réservation a été créée"}