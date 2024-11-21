from typing import List
from uuid import UUID, uuid4

from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from Modele.base import Base

class TypeChambre(Base):
    __tablename__ = "type_chambre"

    id_type_chambre: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True)
    nom_type: Mapped[str] = mapped_column(String(50), nullable=False)
    prix_plafond: Mapped[float] = mapped_column(Float, nullable=False)
    prix_plancher: Mapped[float] = mapped_column(Float, nullable=False)
    description_chambre: Mapped[str] = mapped_column(String(255), nullable=True)

    # Use a string reference to avoid circular import
    chambres: Mapped[List["Chambre"]] = relationship("Modele.chambre.Chambre", back_populates="type_chambre")
