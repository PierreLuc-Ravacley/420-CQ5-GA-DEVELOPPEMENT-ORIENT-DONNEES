from fastapi import FastAPI
from Metier.chambreMetier import  get_reservations, creer_reservation
from DTO.chambreDTO import ReservationDTO


app = FastAPI()

    
@app.get("/reservations/")
def read_reservations():
    return get_reservations()

@app.post("/creerReservation/")
def create_reservation(reservation: ReservationDTO):
    return creer_reservation(reservation)