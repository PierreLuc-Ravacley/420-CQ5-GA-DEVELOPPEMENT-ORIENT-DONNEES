from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Metier.chambreMetier import creerChambre, creerTypeChambre, getChambreParNumero, ChambreDTO, TypeChambreDTO

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify the origins here (e.g., "http://localhost:3000")
    allow_credentials=True,
    allow_methods=["*"],  # You can specify which methods are allowed
    allow_headers=["*"],  # You can specify which headers are allowed
)
    
@app.get("/chambres/{no_chambre}")
def read_item(no_chambre: int):
    return getChambreParNumero(no_chambre)
    
@app.post("/creerTypeChambre")
def read_item(type: TypeChambreDTO):
    return creerTypeChambre(type)
    
@app.post("/creerChambre")
def read_item(chambre: ChambreDTO):
    return creerChambre(chambre)
    