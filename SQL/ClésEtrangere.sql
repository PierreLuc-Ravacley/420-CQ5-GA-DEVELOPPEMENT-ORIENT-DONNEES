USE [hotelDB]
GO

/****** Add foreign key constraints ******/
/* Assuming that these foreign key constraints are intended to establish relationships between tables */

-- Adding foreign key constraint to the Chambre table
ALTER TABLE [dbo].[Chambre]  WITH CHECK ADD  CONSTRAINT [FK_Chambre_Chambre] FOREIGN KEY([numChambre])
REFERENCES [dbo].[Chambre] ([numChambre])
GO
ALTER TABLE [dbo].[Chambre] CHECK CONSTRAINT [FK_Chambre_Chambre]
GO
ALTER TABLE [dbo].[Reservation]  WITH CHECK ADD  CONSTRAINT [FK_Reservation_Reservation] FOREIGN KEY([numReservation])
REFERENCES [dbo].[Reservation] ([numReservation])
GO
ALTER TABLE [dbo].[Reservation] CHECK CONSTRAINT [FK_Reservation_Reservation]
GO
ALTER TABLE [dbo].[TypeChambre]  WITH CHECK ADD  CONSTRAINT [FK_TypeChambre_TypeChambre] FOREIGN KEY([numTypeChambre])
REFERENCES [dbo].[TypeChambre] ([numTypeChambre])
GO
ALTER TABLE [dbo].[TypeChambre] CHECK CONSTRAINT [FK_TypeChambre_TypeChambre]
GO
ALTER TABLE [dbo].[TypeChambre]  WITH CHECK ADD  CONSTRAINT [FK_TypeChambre_TypeChambre1] FOREIGN KEY([numTypeChambre])
REFERENCES [dbo].[TypeChambre] ([numTypeChambre])
GO
ALTER TABLE [dbo].[TypeChambre] CHECK CONSTRAINT [FK_TypeChambre_TypeChambre1]
GO
ALTER TABLE [dbo].[TypeChambre]  WITH CHECK ADD  CONSTRAINT [FK_TypeChambre_TypeChambre2] FOREIGN KEY([numTypeChambre])
REFERENCES [dbo].[TypeChambre] ([numTypeChambre])
GO
ALTER TABLE [dbo].[TypeChambre] CHECK CONSTRAINT [FK_TypeChambre_TypeChambre2]
GO
USE [master]
GO
ALTER DATABASE [hotelDB] SET  READ_WRITE 
GO