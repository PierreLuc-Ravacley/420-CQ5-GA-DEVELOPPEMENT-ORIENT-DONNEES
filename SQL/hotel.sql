USE [master]
GO

/****** Object:  Database [Hotel]    Script Date: 2024-09-04 09:51:29 ******/
CREATE DATABASE [Hotel]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'Hotel', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS01\MSSQL\DATA\Hotel.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'Hotel_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS01\MSSQL\DATA\Hotel_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO

IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [Hotel].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO

ALTER DATABASE [Hotel] SET ANSI_NULL_DEFAULT OFF 
GO

ALTER DATABASE [Hotel] SET ANSI_NULLS OFF 
GO

ALTER DATABASE [Hotel] SET ANSI_PADDING OFF 
GO

ALTER DATABASE [Hotel] SET ANSI_WARNINGS OFF 
GO

ALTER DATABASE [Hotel] SET ARITHABORT OFF 
GO

ALTER DATABASE [Hotel] SET AUTO_CLOSE OFF 
GO

ALTER DATABASE [Hotel] SET AUTO_SHRINK OFF 
GO

ALTER DATABASE [Hotel] SET AUTO_UPDATE_STATISTICS ON 
GO

ALTER DATABASE [Hotel] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO

ALTER DATABASE [Hotel] SET CURSOR_DEFAULT  GLOBAL 
GO

ALTER DATABASE [Hotel] SET CONCAT_NULL_YIELDS_NULL OFF 
GO

ALTER DATABASE [Hotel] SET NUMERIC_ROUNDABORT OFF 
GO

ALTER DATABASE [Hotel] SET QUOTED_IDENTIFIER OFF 
GO

ALTER DATABASE [Hotel] SET RECURSIVE_TRIGGERS OFF 
GO

ALTER DATABASE [Hotel] SET  DISABLE_BROKER 
GO

ALTER DATABASE [Hotel] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO

ALTER DATABASE [Hotel] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO

ALTER DATABASE [Hotel] SET TRUSTWORTHY OFF 
GO

ALTER DATABASE [Hotel] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO

ALTER DATABASE [Hotel] SET PARAMETERIZATION SIMPLE 
GO

ALTER DATABASE [Hotel] SET READ_COMMITTED_SNAPSHOT OFF 
GO

ALTER DATABASE [Hotel] SET HONOR_BROKER_PRIORITY OFF 
GO

ALTER DATABASE [Hotel] SET RECOVERY SIMPLE 
GO

ALTER DATABASE [Hotel] SET  MULTI_USER 
GO

ALTER DATABASE [Hotel] SET PAGE_VERIFY CHECKSUM  
GO

ALTER DATABASE [Hotel] SET DB_CHAINING OFF 
GO

ALTER DATABASE [Hotel] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO

ALTER DATABASE [Hotel] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO

ALTER DATABASE [Hotel] SET DELAYED_DURABILITY = DISABLED 
GO

ALTER DATABASE [Hotel] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO

ALTER DATABASE [Hotel] SET QUERY_STORE = OFF
GO

ALTER DATABASE [Hotel] SET  READ_WRITE 
GO

