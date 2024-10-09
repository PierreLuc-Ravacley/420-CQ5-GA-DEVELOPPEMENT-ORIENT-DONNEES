from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship, mapped_column
from uuid import UUID, uuid4
from Modele.chambre import Chambre, Client

class Base(DeclarativeBase):
    pass

    
class Reservation(Base):
    __tablename__ = "reservation"

    date_fin_reservation: Mapped[str]
    date_debut_reservation: Mapped[str]
    prix_jour: Mapped[float]
    info_reservation: Mapped[str]
    id_reservation: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True)
    fk_id_client: Mapped[str] = mapped_column(ForeignKey("client.id_client"))
    fk_id_chambre: Mapped[str] = mapped_column(ForeignKey("chambre.id_chambre"))

    client: Mapped['Client'] = relationship()
    chambre: Mapped['Chambre'] = relationship()
    
