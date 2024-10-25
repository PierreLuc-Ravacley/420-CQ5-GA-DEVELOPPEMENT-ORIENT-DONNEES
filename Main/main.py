from fastapi import FastAPI
from Metier.chambreMetier import creerChambre, creerTypeChambre, getChambreParNumero, ChambreDTO, TypeChambreDTO
from DTO.reservationDTO import ReservationDTO
from Metier.reservationMetier import get_reservations, creer_reservation,supprimer_reservation
import logging
from uuid import UUID
from fastapi import HTTPException

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
        # Ajoute une trace d'exception complète pour le debug
        logging.error(f"Erreur lors de la création de la réservation: {e}", exc_info=True)
        return {"error": f"Erreur interne : {str(e)}"}  # Affiche le message d'erreur réel




@app.delete("/supprimerReservation/{id_reservation}")
def delete_reservation(id_reservation: UUID):
    try:
        return supprimer_reservation(id_reservation)
    except Exception as e:
        logging.error(f"Erreur lors de la suppression de la réservation: {e}", exc_info=True)
        raise HTTPException(status_code=400, detail=str(e))

