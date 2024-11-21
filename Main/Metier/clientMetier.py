from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select
from DTO.clientDTO import ClientDTO
from Modele.client import Client
from sqlalchemy.exc import IntegrityError

# Connection à la base de données
engine = create_engine('mssql+pyodbc://DESKTOP-6H6E5UF\\SQLEXPRESS/Hotel?driver=SQL Server', use_setinputsizes=False)

def creerClient(client: ClientDTO):
    with Session(engine) as session:
        # Vérifier l'unicité du courriel et du numéro de mobile
        courriel_existe = session.query(Client).filter_by(courriel=client.courriel).first()
        mobile_existe = session.query(Client).filter_by(mobile=client.mobile).first()

        if courriel_existe:
            raise ValueError("Le courriel est déjà utilisé.")
        if mobile_existe:
            raise ValueError("Le numéro de mobile est déjà utilisé.")

        try:
            # Créer un nouvel objet Client
            nouveau_client = Client(
                prenom=client.prenom,
                nom=client.nom,
                adresse=client.adresse,
                mobile=client.mobile,
                mot_de_passe=client.mot_de_passe,
                courriel=client.courriel
            )

            # Ajouter et valider le nouveau client dans la base de données
            session.add(nouveau_client)
            session.commit()

            # Retourner les informations du client nouvellement créé
            return client
        
        except IntegrityError:
            session.rollback()
            raise ValueError("Erreur lors de la création du client/usager.")
        
def getClientParNom(telephone_client: str):
    with Session(engine) as session:
        stmt = select(Client).where(Client.mobile == telephone_client)
        result = session.execute(stmt)
        
        for client in result.scalars():
            return ClientDTO.from_orm(client)



def modifierClient(telephone_client: str, client_data: ClientDTO):
    with Session(engine) as session:
        # Vérifier si le client existe par prénom
        client_exist = session.query(Client).filter(Client.mobile == telephone_client).first()
        
        if not client_exist:
            raise ValueError("Client non trouvé.")

        # Vérifier l'unicité du courriel et du numéro de mobile
        courriel_existe = session.query(Client).filter(Client.courriel == client_data.courriel, Client.id_client != client_exist.id_client).first()
        mobile_existe = session.query(Client).filter(Client.mobile == client_data.mobile, Client.id_client != client_exist.id_client).first()

        if courriel_existe:
            raise ValueError("Le courriel est déjà utilisé.")
        if mobile_existe:
            raise ValueError("Le numéro de mobile est déjà utilisé.")

        try:
            # Mettre à jour les informations du client
            client_exist.prenom = client_data.prenom
            client_exist.nom = client_data.nom
            client_exist.adresse = client_data.adresse
            client_exist.mobile = client_data.mobile
            client_exist.mot_de_passe = client_data.mot_de_passe  # Si le mot de passe doit être mis à jour
            client_exist.courriel = client_data.courriel

            # Valider les modifications dans la base de données
            session.commit()

            # Retourner les informations du client modifié
            return client_data

        except IntegrityError:
            session.rollback()
            raise ValueError("Erreur lors de la mise à jour du client/usager.")