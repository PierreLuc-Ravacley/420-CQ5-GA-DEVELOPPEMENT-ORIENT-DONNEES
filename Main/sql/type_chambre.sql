USE [Hotel]
GO

/****** Object:  Table [dbo].[type_chambre]    Script Date: 2024-09-04 09:53:56 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[type_chambre](
	[nom_type] [varchar](50) NOT NULL,
	[prix_plancher] [money] NOT NULL,
	[prix_plafond] [nchar](10) NULL,
	[description_chambre] [varchar](200) NULL,
	[id_type_chambre] [uniqueidentifier] NOT NULL,
 CONSTRAINT [PK_type_chambre] PRIMARY KEY CLUSTERED 
(
	[id_type_chambre] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

