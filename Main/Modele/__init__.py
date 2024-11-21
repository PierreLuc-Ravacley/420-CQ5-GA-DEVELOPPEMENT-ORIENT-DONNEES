from Modele.base import Base
from Modele.client import Client
from Modele.reservation import Reservation
from Modele.chambre import Chambre
from Modele.typeChambre import TypeChambre

# Ensures all models are loaded for metadata
__all__ = ["Base", "Client", "Reservation", "Chambre", "TypeChambre"]
