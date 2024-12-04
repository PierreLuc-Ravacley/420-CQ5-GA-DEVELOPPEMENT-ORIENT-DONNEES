from typing import List, Annotated
from uuid import UUID
import logging

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

from database import engine  # Import centralized engine
from Modele.base import Base  # Ensure shared Base is loaded

from Metier.chambreMetier import (
    creerChambre,
    getChambreParNumero,
    rechercherChambreLibre,
    ChambreDTO,
)

from Metier.typeChambreMetier import creerTypeChambre, TypeChambreDTO
from Metier.reservationMetier import (
    creer_reservation,
    modifier_reservation,
    supprimer_reservation,
    rechercher_reservation,
)
from Metier.clientMetier import creerClient, getClientParNom, modifierClient, ClientDTO
from DTO.reservationDTO import ReservationDTO, CriteresRechercheDTO

# Fake database for authentication (for demo purposes only)
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
    },
}

# Initialize FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables (only needed during initial setup)
Base.metadata.create_all(bind=engine)



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Logging configuration
logging.basicConfig(level=logging.INFO)


# Authentication Routes
@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": user.username, "token_type": "bearer"}


def fake_hash_password(password: str):
    return "fakehashed" + password


def fake_decode_token(token):
    # Fake decoding logic
    return get_user(fake_users_db, token)


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None


class UserInDB(User):
    hashed_password: str


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


# Chambre Endpoints
@app.get("/chambres/{no_chambre}")
def get_chambre(no_chambre: int):
    return getChambreParNumero(no_chambre)


@app.post("/creerTypeChambre")
def create_type_chambre(type: TypeChambreDTO):
    return creerTypeChambre(type)


@app.post("/creerChambre")
def create_chambre(chambre: ChambreDTO):
    return creerChambre(chambre)


@app.post("/rechercherChambreLibre")
def search_free_chambre(critere: CriteresRechercheDTO):
    try:
        return rechercherChambreLibre(critere)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


# Reservation Endpoints
@app.post("/creerReservation")
def create_reservation(reservation: ReservationDTO):
    try:
        logging.info(f"Création de la réservation: {reservation}")
        return creer_reservation(reservation)
    except Exception as e:
        logging.error(f"Erreur lors de la création de la réservation: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Erreur interne")


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


@app.post("/rechercherReservation")
def search_reservation(criteres: CriteresRechercheDTO):
    try:
        return rechercher_reservation(criteres)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


# Client Endpoints
@app.post("/creerClient")
def create_client(client: ClientDTO):
    return creerClient(client)


@app.get("/verifierClient/{telephone_client}", response_model=ClientDTO)
def get_client_for_verification(
    telephone_client: str, current_user: Annotated[User, Depends(get_current_user)]
):
    client = getClientParNom(telephone_client)
    if not client:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return client


@app.put("/modifierClient/{telephone_client}", response_model=ClientDTO)
def modify_client(telephone_client: str, client_data: ClientDTO):
    try:
        return modifierClient(telephone_client, client_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# Main Application Entry Point
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)