USE [hotelDB]
GO
/****** Object:  Table [dbo].[Chambre]    Script Date: 2024-09-06 1:49:27 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Chambre](
	[numChambre] [uniqueidentifier] NOT NULL,
	[numDePorteChambre] [int] NOT NULL,
	[etatChambre] [bit] NOT NULL,
	[autresInformationsChambre] [varchar](max) NULL,
	[fkNumReservation] [uniqueidentifier] NOT NULL,
 CONSTRAINT [PK_Chambre] PRIMARY KEY CLUSTERED 
(
	[numChambre] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Client]    Script Date: 2024-09-06 1:49:27 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Client](
	[numClient] [uniqueidentifier] NOT NULL,
	[prenomClient] [varchar](50) NOT NULL,
	[nomClient] [varchar](50) NOT NULL,
	[adresseResidenceClient] [varchar](100) NOT NULL,
	[telephoneMobileClient] [varchar](15) NOT NULL,
	[courrielClient] [nvarchar](50) NOT NULL,
	[motDePasseClient] [char](60) NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Reservation]    Script Date: 2024-09-06 1:49:27 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Reservation](
	[numReservation] [uniqueidentifier] NOT NULL,
	[dateDebutReservation] [datetime] NOT NULL,
	[dateFinReservation] [datetime] NOT NULL,
	[prixParJour] [int] NOT NULL,
	[autresInformationsReservation] [text] NULL,
	[fkNumClient] [uniqueidentifier] NOT NULL,
 CONSTRAINT [PK_Reservation] PRIMARY KEY CLUSTERED 
(
	[numReservation] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TypeChambre]    Script Date: 2024-09-06 1:49:27 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TypeChambre](
	[numTypeChambre] [uniqueidentifier] NOT NULL,
	[prixPlancherTypeChambre] [money] NOT NULL,
	[prixPlafondTypeChambre] [money] NULL,
	[descriptionTypeChambre] [text] NULL,
	[fkNumTypeChambre] [int] NULL,
	[typeLitTypeChambre] [varchar](25) NULL,
 CONSTRAINT [PK_TypeChambre] PRIMARY KEY CLUSTERED 
(
	[numTypeChambre] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO