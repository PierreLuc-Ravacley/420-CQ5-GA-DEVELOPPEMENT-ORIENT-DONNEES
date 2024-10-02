USE [Hotel]
GO

/****** Object:  Table [dbo].[client]    Script Date: 2024-09-04 09:53:30 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[client](
	[prenom] [varchar](50) NOT NULL,
	[nom] [varchar](50) NOT NULL,
	[adresse] [varchar](100) NOT NULL,
	[mobile] [char](15) NOT NULL,
	[mot_de_passe] [char](60) NOT NULL,
	[id_client] [uniqueidentifier] NOT NULL,
 CONSTRAINT [PK_client] PRIMARY KEY CLUSTERED 
(
	[id_client] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

