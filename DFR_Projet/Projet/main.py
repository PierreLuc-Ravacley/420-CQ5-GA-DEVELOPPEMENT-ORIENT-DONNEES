from fastapi import FastAPI
from Metier.chambreMetier import creerChambre, creerTypeChambre, getChambreParNumero
from Metier.chambreMetier import ChambreDTO, TypeChambreDTO,ClientDTO,ReservationDT0

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

@app.get("/clients/")
def read_clients():
    return get_clients()

@app.post("/creerClient/")
def create_client(client: ClientDTO):
    return creer_client(client)

@app.get("/reservations/")
def read_reservations():
    return get_reservations()

@app.post("/creerReservation/")
def create_reservation(reservation: ReservationDTO):
    return creer_reservation(reservation)
 