from typing import List
from uuid import UUID, uuid4

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from Modele.base import Base


class Client(Base):
    __tablename__ = "client"

    id_client: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True)
    prenom: Mapped[str] = mapped_column(String(50), nullable=False)
    nom: Mapped[str] = mapped_column(String(50), nullable=False)
    adresse: Mapped[str] = mapped_column(String(255), nullable=True)
    mobile: Mapped[str] = mapped_column(String(15), unique=True, nullable=False)
    mot_de_passe: Mapped[str] = mapped_column(String(255), nullable=False)
    courriel: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)

    # Use a string reference to avoid circular import
    reservations: Mapped[List["Reservation"]] = relationship("Modele.reservation.Reservation", back_populates="client")
