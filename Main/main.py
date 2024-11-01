from typing import Annotated
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from Metier.chambreMetier import creerChambre, creerTypeChambre, getChambreParNumero, ChambreDTO, TypeChambreDTO
from DTO.reservationDTO import ReservationDTO, CriteresRechercheDTO
from Metier.reservationMetier import creer_reservation, modifier_reservation, supprimer_reservation, rechercher_reservation
import logging
from uuid import UUID
import uvicorn

# Base de données fictive des utilisateurs
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret"
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2"
    },
}

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Fonctions et classes utilitaires liées à la sécurité
def fake_hash_password(password: str):
    return "fakehashed" + password

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None

class UserInDB(User):
    hashed_password: str

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def fake_decode_token(token):
    user = get_user(fake_users_db, token)
    return user

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

# Route de connexion pour obtenir le token
@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if hashed_password != user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": user.username, "token_type": "bearer"}

# Routes de gestion des chambres
@app.get("/chambres/{no_chambre}")
def read_item(no_chambre: int):
    return getChambreParNumero(no_chambre)
    
@app.post("/creerTypeChambre")
def read_item(type: TypeChambreDTO):
    return creerTypeChambre(type)
    
@app.post("/creerChambre")
def read_item(chambre: ChambreDTO):
    return creerChambre(chambre)

# Routes de gestion des réservations avec vérification de l'utilisateur
logging.basicConfig(level=logging.INFO)

@app.post("/creerReservation/")
def create_reservation(reservation: ReservationDTO, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        logging.info(f"Création de la réservation: {reservation}")
        return creer_reservation(reservation)
    except Exception as e:
        logging.error(f"Erreur lors de la création de la réservation: {e}", exc_info=True)
        return {"error": f"Erreur interne : {str(e)}"}

@app.put("/modifierReservation/{id_reservation}")
def update_reservation(id_reservation: UUID, reservation: ReservationDTO, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        return modifier_reservation(id_reservation, reservation)
    except Exception as e:
        logging.error(f"Erreur lors de la modification de la réservation: {e}", exc_info=True)
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/supprimerReservation/{id_reservation}")
def delete_reservation(id_reservation: UUID, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        return supprimer_reservation(id_reservation)
    except Exception as e:
        logging.error(f"Erreur lors de la suppression de la réservation: {e}", exc_info=True)
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/rechercherReservation/")
def search_reservation(criteres: CriteresRechercheDTO, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        return rechercher_reservation(criteres)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    uvicorn.run(app, host="127.0.0.1", port=8000)
