USE [hotelDB]
GO

-- Déclarer une variable pour l'ID unique
DECLARE @id uniqueidentifier

-- Insérer un enregistrement pour un type de chambre 'simple'
SET @id = NEWID()
INSERT INTO [dbo].[TypeChambre]
           ([numTypeChambre]
           ,[prixPlancherTypeChambre]
           ,[prixPlafondTypeChambre]
           ,[descriptionTypeChambre]
           ,[fkNumTypeChambre])
     VALUES
           (@id
           ,99
           ,199
           ,'Chambre avec un seul lit simple'
           ,NULL) -- Remplacer NULL par une valeur appropriée si nécessaire

-- Insérer un enregistrement pour un type de chambre 'double'
SET @id = NEWID()
INSERT INTO [dbo].[TypeChambre]
           ([numTypeChambre]
           ,[prixPlancherTypeChambre]
           ,[prixPlafondTypeChambre]
           ,[descriptionTypeChambre]
           ,[fkNumTypeChambre])
     VALUES
           (@id
           ,129
           ,229
           ,'Chambre avec un seul lit double'
           ,NULL) -- Remplacer NULL par une valeur appropriée si nécessaire

-- Insérer un enregistrement pour un type de chambre 'queen'
SET @id = NEWID()
INSERT INTO [dbo].[TypeChambre]
           ([numTypeChambre]
           ,[prixPlancherTypeChambre]
           ,[prixPlafondTypeChambre]
           ,[descriptionTypeChambre]
           ,[fkNumTypeChambre])
     VALUES
           (@id
           ,159
           ,279
           ,'Chambre avec un seul lit queen'
           ,NULL) -- Remplacer NULL par une valeur appropriée si nécessaire

-- Insérer un enregistrement pour un type de chambre 'king'
SET @id = NEWID()
INSERT INTO [dbo].[TypeChambre]
           ([numTypeChambre]
           ,[prixPlancherTypeChambre]
           ,[prixPlafondTypeChambre]
           ,[descriptionTypeChambre]
           ,[fkNumTypeChambre])
     VALUES
           (@id
           ,179
           ,329
           ,'Chambre avec un seul lit king'
           ,NULL) -- Remplacer NULL par une valeur appropriée si nécessaire
GO

