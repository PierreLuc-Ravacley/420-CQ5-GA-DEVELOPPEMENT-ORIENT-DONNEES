from fastapi import FastAPI
from pydantic import BaseModel

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import select

from Modele.chambre import Chambre, TypeChambre, Client,Reservation

# Configure the SQLAlchemy engine
DATABASE_URL = 'mssql+pyodbc://DESKTOP-6KMCBC1\\SQLEXPRESS01/Hotel?driver=SQL Server'
engine = create_engine(DATABASE_URL, use_setinputsizes=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

# Data Transfer Object : pydantic BaseModel pour intégration facile avec FastAPI
class TypeChambreDTO(BaseModel): 
    nom_type: str
    prix_plafond: float
    prix_plancher: float
    description_chambre : str

class ChambreDTO(BaseModel): 
    numero_chambre: int
    disponible_reservation : bool
    autre_informations: str
    type_chambre: str

class ClientDTO(BaseModel):  # Create a ClientDTO for easy integration with FastAPI
    prenom: str
    nom: str
    adresse: str
    mobile: str
    mot_de_passe: str
    
@app.get("/chambres/{no_chambre}")
def read_item(no_chambre: int):
    with Session(engine) as session:
        stmt = select(Chambre).where(Chambre.numero_chambre == no_chambre)
        result = session.execute(stmt)
        for chambre in result.scalars():
             print(f"{chambre.numero_chambre} {chambre.type_chambre.nom_type} {len(chambre.type_chambre.chambres)}")
        
        return {"numéro de chambre": chambre.numero_chambre,
                "type_chambre" : chambre.type_chambre.nom_type}
    
@app.post("/creerTypeChambre")
def read_item(type: TypeChambreDTO):
    with Session(engine) as session:
        nouveauTypeChambre = TypeChambre (
            nom_type = type.nom_type,
            prix_plafond = type.prix_plafond,
            prix_plancher = type.prix_plancher,
            description_chambre = type.description_chambre
        )

        session.add(nouveauTypeChambre)
        session.commit()
        
        return type

@app.post("/creerChambre")
def read_item(chambre: ChambreDTO):
    with Session(engine) as session:
        stmt = select(TypeChambre).where(TypeChambre.nom_type == chambre.type_chambre)
        result = session.execute(stmt)
        
        for typeChambre in result.scalars():
            
            nouvelleChambre = Chambre (
            numero_chambre = chambre.numero_chambre,
            disponible_reservation = chambre.disponible_reservation,
            autre_informations = chambre.autre_informations,
            type_chambre = typeChambre
            )

            session.add(nouvelleChambre)
            session.commit()
        
        return chambre
    
@app.post("/creerClients/")  # client creation
def create_client(client: ClientDTO):
    with Session(engine) as session:
        new_client = Client(**client.dict())  # new Client instance
        session.add(new_client)
        session.commit()
        return {"message": "Le client a été creer"} 