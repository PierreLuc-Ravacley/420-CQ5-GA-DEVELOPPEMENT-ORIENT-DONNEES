USE [hotelDB]
GO

DECLARE @pk uniqueidentifier
DECLARE @id_type_choisi INT;
DECLARE @uuid_choisi uniqueidentifier;
DECLARE @liste_id_type_chambre table (id int, value uniqueidentifier);

-- Chaque value doit être remplacée par les UID que vous avez généré dans la table [dbo].[type_chambre]
INSERT @liste_id_type_chambre(id, value) VALUES(1,'1C3D9B64-50E8-454B-B801-2F4888FDEC8B'), 
                                               (2,'D8224AF9-9369-4E0E-8F91-79F846756314'), 
                                               (3,'78772BDF-1D0D-4E2B-ABB9-8E0C888E8862'), 
                                               (4,'9D33232D-5536-4CD1-A757-C41B8B462D72');

DECLARE @i int = 1;
WHILE @i <= 500
BEGIN
    SET @pk = NEWID()
    SET @id_type_choisi = (SELECT CAST(RAND()*(4-1)+1 AS INT));
    SET @uuid_choisi = (select value from @liste_id_type_chambre where id = @id_type_choisi);

    INSERT INTO [dbo].[Chambre]
               ([numChambre]
               ,[numDePorteChambre]
               ,[etatChambre]
               ,[autresInformationsChambre]
               ,[fkNumReservation])
         VALUES
               (@pk
               ,@i
               ,1
               ,NULL
               ,@uuid_choisi)

    SET @i = @i + 1;
END
GO