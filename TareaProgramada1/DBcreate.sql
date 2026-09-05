USE master;
GO
 
IF DB_ID('BD_Empleados') IS NULL
BEGIN
    CREATE DATABASE BD_Empleados;
END
GO
 
USE BD_Empleados;
GO