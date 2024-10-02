USE [Hotel]
GO

/****** Object:  Table [dbo].[reservation]    Script Date: 2024-09-04 09:53:44 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[reservation](
	[date_fin_reservation] [datetime] NOT NULL,
	[date_debut_reservation] [datetime] NOT NULL,
	[prix_jour] [money] NOT NULL,
	[info_reservation] [varchar](max) NULL,
	[id_reservation] [uniqueidentifier] NOT NULL,
	[fk_id_client] [uniqueidentifier] NOT NULL,
	[fk_id_chambre] [uniqueidentifier] NULL,
 CONSTRAINT [PK_reservation] PRIMARY KEY CLUSTERED 
(
	[id_reservation] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
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