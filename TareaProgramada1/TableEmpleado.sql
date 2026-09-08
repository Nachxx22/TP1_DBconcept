USE BD_Empleados;
IF OBJECT_ID('dbo.Empleado', 'U') IS NOT NULL
    DROP TABLE dbo.Empleado;
GO
 
CREATE TABLE dbo.Empleado
(
    Id      INT IDENTITY(1, 1) PRIMARY KEY,
    Nombre  VARCHAR(128) NOT NULL,
    Salario MONEY        NOT NULL
);
GO

--Select * from dbo.Empleado;


--Carga de datos de prueba (40 filas)
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Juan Perez', 200000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Ana Rojas', 250000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Luis Chaves', 200000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Maria Gonzalez', 310000.50);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Carlos Vargas', 275000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Sofia Jimenez', 320000.75);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Diego Mora', 180000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Valeria Solano', 295000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Andres Castro', 260000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Paula Arguedas', 305000.25);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Kevin Salas', 210000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Fabiola Mena', 330000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Esteban Quiros', 245000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Daniela Brenes', 290000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Jose Fonseca', 199000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Karla Vindas', 315000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Mauricio Solis', 265000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Gabriela Zamora', 275000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Ricardo Alvarado', 240000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Melissa Rodriguez', 300000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Alejandro Barrantes', 285000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Natalia Chinchilla', 255000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Gustavo Sanchez', 220000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Silvia Marin', 310000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Roberto Duran', 190000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Tatiana Herrera', 325000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Manuel Villalobos', 235000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Adriana Cordero', 280000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Felipe Camacho', 205000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Vanessa Ramirez', 260000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Oscar Hidalgo', 215000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Priscilla Navarro', 335000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Jorge Aguilar', 225000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Monica Cruz', 270000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Sebastian Guzman', 230000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Laura Portuguez', 300000.50);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Ivan Rojas', 195000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Cristina Ureña', 288000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Pablo Segura', 250000.00);
INSERT INTO dbo.Empleado (Nombre, Salario) VALUES ('Rebeca Blanco', 312000.00);
GO
