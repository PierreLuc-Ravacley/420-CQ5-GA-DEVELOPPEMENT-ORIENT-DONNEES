from fastapi import FastAPI
from Metier.chambreMetier import creerChambre, creerTypeChambre, getChambreParNumero, ChambreDTO, TypeChambreDTO
from DTO.reservationDTO import ReservationDTO
from Metier.reservationMetier import get_reservations, creer_reservation
import logging

app = FastAPI()

    
@app.get("/chambres/{no_chambre}")
def read_item(no_chambre: int):
    return getChambreParNumero(no_chambre)
    
@app.post("/creerTypeChambre")
def read_item(type: TypeChambreDTO):
    return creerTypeChambre(type)
    
@app.post("/creerChambre")
def read_item(chambre: ChambreDTO):
    return creerChambre(chambre)

@app.get("/reservations/")
def read_reservations():
    return get_reservations()

logging.basicConfig(level=logging.INFO)

@app.post("/creerReservation/")
def create_reservation(reservation: ReservationDTO):
    try:
        logging.info(f"Création de la réservation: {reservation}")
        return creer_reservation(reservation)
    except Exception as e:
        # Ajoutez une trace d'exception complète pour le debug
        logging.error(f"Erreur lors de la création de la réservation: {e}", exc_info=True)
        return {"error": f"Erreur interne : {str(e)}"}  # Affichez le message d'erreur réel

