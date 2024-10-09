from pydantic import BaseModel
from Modele.chambre import Client

# Data Transfer Object : Pydantic BaseModel pour une intégration facile avec FastAPI
class ClientDTO(BaseModel):
    prenom: str
    nom: str
    adresse: str
    mobile: str
    mot_de_passe: str
    courriel: str

    # Configuration Pydantic pour la compatibilité avec l'ORM
    class Config:
        orm_mode = True

    # Méthode de classe pour créer un DTO à partir d'un objet Client (entité ORM)
    @classmethod
    def from_orm(cls, client: Client):
        return cls(
            prenom=client.prenom,
            nom=client.nom,
            adresse=client.adresse,
            mobile=client.mobile,
            mot_de_passe=client.mot_de_passe,
            courriel=client.courriel
        )


        