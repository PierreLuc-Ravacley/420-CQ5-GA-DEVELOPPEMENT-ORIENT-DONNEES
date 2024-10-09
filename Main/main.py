from fastapi import FastAPI
from Metier.chambreMetier import creerChambre, creerTypeChambre, getChambreParNumero, ChambreDTO, TypeChambreDTO
from Metier.clientMetier import creerClient, modifierClient, ClientDTO

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

@app.post("/creerClient")
def read_item(client: ClientDTO):
    return creerClient(client)

@app.post("/modifierClient{Prenom}")
def read_item(client: ClientDTO):
    return modifierClient(client)