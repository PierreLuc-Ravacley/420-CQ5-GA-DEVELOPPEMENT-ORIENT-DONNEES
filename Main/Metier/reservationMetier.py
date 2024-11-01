from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select
from DTO.reservationDTO import ReservationDTO, CriteresRechercheDTO
from Modele.reservation import Reservation
from Modele.chambre import Chambre,Client
from uuid import UUID
from datetime import datetime
from sqlalchemy.exc import NoResultFound

engine = create_engine('mssql+pyodbc://DESKTOP-6KMCBC1\\SQLEXPRESS01/Hotel?driver=SQL Server', use_setinputsizes=False)


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
            date_debut_reservation=datetime.combine(reservation.dateDebut, datetime.min.time()),  
            date_fin_reservation=datetime.combine(reservation.dateFin, datetime.min.time()),     
            prix_jour=reservation.prixParJour,
            info_reservation=reservation.infoReservation
        )

        session.add(nouvelle_reservation)
        session.commit()

        # Récupére la réservation nouvellement créée depuis la base de données
        reservation_cree = session.execute(select(Reservation).where(Reservation.id_reservation == nouvelle_reservation.id_reservation)).scalar_one()

        # Converti la réservation créée en ReservationDTO
        reservation_dto = ReservationDTO.from_model(reservation_cree)

        return reservation_dto
    
def modifier_reservation(id_reservation: UUID, reservation: ReservationDTO):
    with Session(engine) as session:
        # Vérifie si la réservation existe
        existing_reservation = session.execute(select(Reservation).where(Reservation.id_reservation == id_reservation)).scalar_one_or_none()
        if existing_reservation is None:
            raise ValueError("La réservation n'existe pas.")

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
            Reservation.id_reservation != id_reservation,  # Ignore la réservation actuelle
            Reservation.date_debut_reservation < reservation.dateFin,
            Reservation.date_fin_reservation > reservation.dateDebut
        )
        if session.execute(stmt).first() is not None:
            raise ValueError("La chambre est déjà réservée pendant cette période.")

        # Met à jour la réservation
        existing_reservation.fk_id_client = reservation.fk_id_client
        existing_reservation.fk_id_chambre = reservation.fk_id_chambre
        existing_reservation.date_debut_reservation = datetime.combine(reservation.dateDebut, datetime.min.time())  
        existing_reservation.date_fin_reservation = datetime.combine(reservation.dateFin, datetime.min.time()) 
        existing_reservation.prix_jour = reservation.prixParJour
        existing_reservation.info_reservation = reservation.infoReservation

        session.commit()

        return ReservationDTO.from_model(existing_reservation)


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
    
def rechercher_reservation(criteres: CriteresRechercheDTO):
    with Session(engine) as session:
        stmt = select(Reservation)
        
        # Applique les filtres en fonction des critères de recherche
        if criteres.idReservation:
            stmt = stmt.where(Reservation.id_reservation == UUID(criteres.idReservation))
        if criteres.idClient:
            stmt = stmt.where(Reservation.fk_id_client == UUID(criteres.idClient))
        if criteres.idChambre:
            stmt = stmt.where(Reservation.fk_id_chambre == UUID(criteres.idChambre))
        
        if criteres.nom or criteres.prenom:
            stmt = stmt.join(Client)
            if criteres.nom:
                stmt = stmt.where(Client.nom == criteres.nom)
            if criteres.prenom:
                stmt = stmt.where(Client.prenom == criteres.prenom)
        
        try:
            # Exécute la requête et récupère les résultats
            result = session.execute(stmt).scalars().all()
            if not result:
                raise NoResultFound()
            
            # Convertit les résultats en DTO
            return [ReservationDTO.from_model(reservation) for reservation in result]
        
        except NoResultFound:
            raise ValueError("Aucune réservation trouvée avec les critères spécifiés.")