from typing import List

from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship, mapped_column
from uuid import UUID, uuid4
from datetime import datetime 

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

class Client(Base):
    __tablename__ = "client"

    prenom: Mapped[str]
    nom: Mapped[str]
    adresse: Mapped[str]
    mobile: Mapped[str]
    mot_de_passe: Mapped[str]
    id_client: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True)

class Reservation(Base):
    __tablename__ = "reservation"

    date_fin_reservation: Mapped[datetime]
    date_debut_reservation: Mapped[datetime]
    prix_jour: Mapped[float] = mapped_column(Numeric) 
    info_reservation: Mapped[str]
    id_reservation: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True)
    fk_id_client: Mapped[UUID] = mapped_column(ForeignKey("client.id_client"))
    fk_id_chambre: Mapped[UUID] = mapped_column(ForeignKey("chambre.id_chambre"))

    client: Mapped['Client'] = relationship()
    chambre: Mapped['Chambre'] = relationship()