from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select
from DTO.chambreDTO import ChambreDTO, TypeChambreDTO, ClientDTO, ReservationDTO  # Ajout des DTO manquants
from Modele.chambre import Chambre, TypeChambre, Client, Reservation

engine = create_engine('mssql+pyodbc://DESKTOP-6KMCBC1\\SQLEXPRESS01/Hotel?driver=SQL Server', use_setinputsizes=False)

def creerChambre(chambre: ChambreDTO):
    with Session(engine) as session:
        stmt = select(TypeChambre).where(TypeChambre.nom_type == chambre.type_chambre)
        result = session.execute(stmt)

        for typeChambre in result.scalars():
            nouvelleChambre = Chambre (
                numero_chambre = chambre.numero_chambre,
                disponible_reservation = chambre.disponible_reservation,
                autre_informations = chambre.autre_informations,
                type_chambre = typeChambre
            )

            session.add(nouvelleChambre)
            session.commit()
        
        return chambre

def creerTypeChambre(typeChambre: TypeChambreDTO):
    with Session(engine) as session:
        nouveauTypeChambre = TypeChambre(typeChambre)

        session.add(nouveauTypeChambre)
        session.commit()
        
        return typeChambre

def getChambreParNumero(no_chambre: int):
    with Session(engine) as session:
        stmt = select(Chambre).where(Chambre.numero_chambre == no_chambre)
        result = session.execute(stmt)
        
        for chambre in result.scalars():
            return ChambreDTO(chambre)


def get_clients():
    with Session(engine) as session:
        stmt = select(Client)
        result = session.execute(stmt)
        clients = result.scalars().all()
        return [{"id": c.id_client, "prenom": c.prenom, "nom": c.nom, "adresse": c.adresse, "mobile": c.mobile} for c in clients]

def creer_client(client: ClientDTO):
    with Session(engine) as session:
        new_client = Client(**client.dict())
        session.add(new_client)
        session.commit()
        return {"message": "Le client a été créé"}

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