from fastapi import FastAPI
from Metier.chambreMetier import creerChambre, creerTypeChambre, getChambreParNumero, ChambreDTO, TypeChambreDTO
from DTO.reservationDTO import ReservationDTO,CriteresRechercheDTO
from Metier.reservationMetier import creer_reservation, modifier_reservation,supprimer_reservation,rechercher_reservation
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

@app.put("/modifierReservation/{id_reservation}")
def update_reservation(id_reservation: UUID, reservation: ReservationDTO):
    try:
        return modifier_reservation(id_reservation, reservation)
    except Exception as e:
        logging.error(f"Erreur lors de la modification de la réservation: {e}", exc_info=True)
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/supprimerReservation/{id_reservation}")
def delete_reservation(id_reservation: UUID):
    try:
        return supprimer_reservation(id_reservation)
    except Exception as e:
        logging.error(f"Erreur lors de la suppression de la réservation: {e}", exc_info=True)
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/rechercherReservation/")
def search_reservation(criteres: CriteresRechercheDTO):
    try:
        return rechercher_reservation(criteres)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
