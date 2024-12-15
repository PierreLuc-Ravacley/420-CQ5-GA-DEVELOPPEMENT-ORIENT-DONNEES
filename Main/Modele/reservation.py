from typing import List
from uuid import UUID, uuid4
import datetime

from sqlalchemy import String, Float, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from Modele.base import Base

class Reservation(Base):
    __tablename__ = "reservation"

    id_reservation: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True)
    date_debut_reservation: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)
    date_fin_reservation: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)
    prix_jour: Mapped[float] = mapped_column(Float, nullable=False)
    info_reservation: Mapped[str] = mapped_column(String(255), nullable=True)
    fk_id_client: Mapped[UUID] = mapped_column(ForeignKey("client.id_client"))
    fk_id_chambre: Mapped[UUID] = mapped_column(ForeignKey("chambre.id_chambre"))

    # Use string references to avoid circular import
    client: Mapped["Client"] = relationship("Modele.client.Client", back_populates="reservations")
    chambre: Mapped["Chambre"] = relationship("Modele.chambre.Chambre", back_populates="reservations")
    