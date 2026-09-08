USE BD_Empleados;
GO

-- Si el login existe a nivel servidor pero no tiene usuario en esta BD todavía:
--CREATE USER testsql123 FOR LOGIN testsql123;
--GO

--Para dar poermisos a un ususario especifico de poder utilizar ciertos storeprocedure
--Tiene que ser desde la conexión administrador del SSMS
-- Despues del TO tiene que ser el nombre del usuario/login 
GRANT EXECUTE ON dbo.sp_ObtenerEmpleados TO Maripaz;
GRANT EXECUTE ON dbo.sp_InsertarEmpleado TO Maripaz;
GO