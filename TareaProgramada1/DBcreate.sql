USE master;
GO
 
 --Comprueba si existe la base de datos con el nombre, en el caso de no existir la crea
IF DB_ID('BD_Empleados') IS NULL
BEGIN
    CREATE DATABASE BD_Empleados;
END
GO
 
USE BD_Empleados;
GO