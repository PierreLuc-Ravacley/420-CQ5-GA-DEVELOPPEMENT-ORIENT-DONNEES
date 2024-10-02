USE [Hotel]
GO

DECLARE @id uniqueidentifier
SET @id = NEWID()


INSERT INTO [dbo].[type_chambre]
           ([nom_type]
           ,[prix_plancher]
           ,[prix_plafond]
           ,[description_chambre]
           ,[id_type_chambre])
     VALUES
           ('simple'
           ,99
           ,199
           ,'Chambre avec un seul lit simple'
           ,@id)


SET @id = NEWID()
   INSERT INTO [dbo].[type_chambre]
           ([nom_type]
           ,[prix_plancher]
           ,[prix_plafond]
           ,[description_chambre]
           ,[id_type_chambre])
     VALUES
           ('double'
           ,129
           ,229
           ,'Chambre avec un seul lit double'
           ,@id)


SET @id = NEWID()
   INSERT INTO [dbo].[type_chambre]
           ([nom_type]
           ,[prix_plancher]
           ,[prix_plafond]
           ,[description_chambre]
           ,[id_type_chambre])
     VALUES
           ('queen'
           ,159
           ,279
           ,'Chambre avec un seul lit queen'
           ,@id)


SET @id = NEWID()
   INSERT INTO [dbo].[type_chambre]
           ([nom_type]
           ,[prix_plancher]
           ,[prix_plafond]
           ,[description_chambre]
           ,[id_type_chambre])
     VALUES
           ('king'
           ,179
           ,329
           ,'Chambre avec un seul lit king'
           ,@id)
GO

