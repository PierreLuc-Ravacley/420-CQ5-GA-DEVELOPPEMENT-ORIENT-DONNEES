USE [Hotel]

GO

ALTER TABLE [dbo].[reservation]  WITH CHECK ADD  CONSTRAINT [FK_reservation_chambre] FOREIGN KEY([fk_id_chambre])
REFERENCES [dbo].[chambre] ([id_chambre])
GO

ALTER TABLE [dbo].[reservation] CHECK CONSTRAINT [FK_reservation_chambre]
GO

ALTER TABLE [dbo].[reservation]  WITH CHECK ADD  CONSTRAINT [FK_reservation_client] FOREIGN KEY([fk_id_client])
REFERENCES [dbo].[client] ([id_client])
GO

ALTER TABLE [dbo].[reservation] CHECK CONSTRAINT [FK_reservation_client]
GO

