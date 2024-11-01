from typing import List
from fastapi import FastAPI, HTTPException
from Metier.chambreMetier import creerChambre, getChambreParNumero, ChambreDTO
from Metier.typeChambreMetier import creerTypeChambre, TypeChambreDTO
from Metier.reservationMetier import rechercherReservation
from Metier.chambreMetier import rechercherChambreLibre
from DTO.reservationDTO import CriteresRechercheDTO
from DTO.chambreDTO import CriteresRechercheDTO
import uvicorn

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

@app.post("/rechercherReservation")
def read_item(critere: CriteresRechercheDTO):
    try:
        return rechercherReservation(critere)
    except ValueError as e:
        return HTTPException(status_code=404, detail=str(e))
    
@app.post("/rechercherChambreLibre")
def read_item(critere: CriteresRechercheDTO):
    try:
        return rechercherChambreLibre(critere)
    except ValueError as e:
        return HTTPException(status_code=404, detail=str(e))
 
uvicorn.run(app, host="127.0.0.1", port=8000)
    
    