USE [Hotel]
GO

/****** Object:  Table [dbo].[chambre]    Script Date: 2024-09-04 09:53:18 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[chambre](
	[numero_chambre] [smallint] NOT NULL,
	[disponible_reservation] [bit] NOT NULL,
	[autre_informations] [varchar](max) NULL,
	[id_chambre] [uniqueidentifier] NOT NULL,
	[fk_type_chambre] [uniqueidentifier] NULL,
 CONSTRAINT [PK_chambre] PRIMARY KEY CLUSTERED 
(
	[id_chambre] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

ALTER TABLE [dbo].[chambre]  WITH CHECK ADD  CONSTRAINT [FK_chambre_type_chambre] FOREIGN KEY([fk_type_chambre])
REFERENCES [dbo].[type_chambre] ([id_type_chambre])
GO

ALTER TABLE [dbo].[chambre] CHECK CONSTRAINT [FK_chambre_type_chambre]
GO

