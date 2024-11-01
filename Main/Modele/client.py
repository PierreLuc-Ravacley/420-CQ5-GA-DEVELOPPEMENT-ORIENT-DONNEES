from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship, mapped_column
from uuid import UUID, uuid4

class Base(DeclarativeBase):
    pass

class Client(Base):
    __tablename__ = "client"

    prenom: Mapped[str]
    nom: Mapped[str]
    adresse: Mapped[str]
    mobile: Mapped[str]
    mot_de_passe: Mapped[str]
    courriel: Mapped[str]
    id_client: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True)

    reservations: Mapped[List["Reservation"]] = relationship(back_populates="client") 
