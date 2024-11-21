from typing import List
from uuid import UUID, uuid4

from sqlalchemy import String, Boolean, ForeignKey, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from Modele.base import Base


class Chambre(Base):
    __tablename__ = "chambre"

    id_chambre: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True)
    numero_chambre: Mapped[int] = mapped_column(Integer, nullable=False)
    disponible_reservation: Mapped[bool] = mapped_column(Boolean, nullable=False)
    autre_informations: Mapped[str] = mapped_column(String(255), nullable=True)
    fk_type_chambre: Mapped[str] = mapped_column(ForeignKey("type_chambre.id_type_chambre"))

    # Use string references to avoid circular import
    type_chambre: Mapped["TypeChambre"] = relationship("Modele.typeChambre.TypeChambre", back_populates="chambres")
    reservations: Mapped[List["Reservation"]] = relationship("Modele.reservation.Reservation", back_populates="chambre")
