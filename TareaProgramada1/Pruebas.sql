
USE BD_Empleados;
Select * From dbo.Empleado;

--Para comprobrar el funcionamiento correcto del sp de obtener empleados
 EXEC dbo.sp_ObtenerEmpleados;

 --Para comprobar el funcionamiento correcto de instertar empleo y también comprobar que en caso de duplicado no se inserte un duplicado y devuelva un error
 EXEC dbo.sp_InsertarEmpleado @Nombre = 'Pedro Alfaro', @Salario = 220000.00;
 EXEC dbo.sp_InsertarEmpleado @Nombre = 'Pedro Alfaro', @Salario = 220000.00; -- debe fallar (duplicado) y devolver un codigo de error y mensaje


