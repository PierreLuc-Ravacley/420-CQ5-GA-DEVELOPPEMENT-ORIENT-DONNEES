from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship, mapped_column
from uuid import UUID, uuid4

class Base(DeclarativeBase):
    pass

class Chambre(Base):
    __tablename__ = "chambre"

    numero_chambre: Mapped[int]
    disponible_reservation: Mapped[bool]
    autre_informations: Mapped[str]
    id_chambre: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True)
    fk_type_chambre: Mapped[str] = mapped_column(ForeignKey("type_chambre.id_type_chambre"))

    type_chambre: Mapped['TypeChambre'] = relationship()

class TypeChambre(Base):
    __tablename__ = "type_chambre"

    nom_type: Mapped[str]
    prix_plafond: Mapped[float]
    prix_plancher: Mapped[float]
    description_chambre: Mapped[str]
    id_type_chambre: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True)

    chambres: Mapped[List["Chambre"]] = relationship(back_populates="type_chambre")