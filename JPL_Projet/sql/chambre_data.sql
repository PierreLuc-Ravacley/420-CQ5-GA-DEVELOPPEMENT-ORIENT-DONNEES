USE [Hotel]
GO

DECLARE @pk uniqueidentifier
DECLARE @id_type_choisi INT;
DECLARE @uuid_choisi uniqueidentifier;
DECLARE @liste_id_type_chambre table (id int, value uniqueidentifier);

-- Chaque value doit être remplacée par les UID que vous avez généré dans la table [dbo].[type_chambre]
INSERT @liste_id_type_chambre(id, value) VALUES(1,'D99A8E01-77C1-4AE0-BAD1-9834C8543B3B'),
											   (2,'1455E6E0-0C4E-4BEE-A0A1-8B391FB8C964'),
											   (3,'69AD4531-E324-4327-80FE-B45222796392'),
											   (4,'5AA584F0-DC11-44DB-84F8-4EA5A218FC41');

DECLARE @i int = 1;
WHILE @i <= 500
BEGIN
	SET @pk = NEWID()
	SET @id_type_choisi = (SELECT CAST(RAND()*(4-1)+1 AS INT));
	SET @uuid_choisi = (select value from @liste_id_type_chambre where id = @id_type_choisi);

	INSERT INTO [dbo].[chambre]
			   ([numero_chambre]
			   ,[disponible_reservation]
			   ,[autre_informations]
			   ,[id_chambre]
			   ,[fk_type_chambre])
		 VALUES
			   (@i
			   ,1
			   ,NULL
			   ,@pk
			   ,@uuid_choisi)
	SET @i = @i + 1;
END
GO

USE [Hotel]
BEGIN
DELETE [dbo].[chambre];
END
