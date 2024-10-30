from fastapi import FastAPI, HTTPException
from Metier.chambreMetier import creerChambre, creerTypeChambre, getChambreParNumero, ChambreDTO, TypeChambreDTO
from Metier.clientMetier import creerClient, getClientParNom, modifierClient, ClientDTO


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

# Endpoint pour obtenir un client par son prénom, avant de faire la modification
@app.get("/verifierClient/{telephone_client}", response_model=ClientDTO)
def get_client_for_verification(telephone_client: str):
    client = getClientParNom(telephone_client)
    if not client:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    # Retourne les informations actuelles du client pour vérification
    return client



# Endpoint pour modifier un client par son prénom
@app.put("/modifierClient/{telephone_client}", response_model=ClientDTO)
def modify_client(telephone_client: str, client_data: ClientDTO):
    try:
        # Appel de la fonction métier pour modifier les données du client
        updated_client = modifierClient(telephone_client, client_data)
        return updated_client
    except ValueError as e:
        # Si une erreur survient, elle sera envoyée sous forme d'exception HTTP
        raise HTTPException(status_code=400, detail=str(e))