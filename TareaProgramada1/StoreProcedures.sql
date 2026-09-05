USE BD_Empleados;
GO

-- 4. SP: Listar empleados en orden alfabético por nombre
CREATE OR ALTER PROCEDURE dbo.sp_ObtenerEmpleados
AS
BEGIN
    SET NOCOUNT ON;

    BEGIN TRY
        SELECT
            e.Id,
            e.Nombre,
            e.Salario
        FROM
            dbo.Empleado AS e
        ORDER BY
            e.Nombre ASC;
    END TRY
    BEGIN CATCH
        SELECT
            ERROR_NUMBER()  AS CodigoError,
            ERROR_MESSAGE() AS Mensaje;
    END CATCH

    SET NOCOUNT OFF;
END
GO

-- 5. SP: Insertar un empleado nuevo
--    - Valida duplicados manualmente (NO con índice unique)
--    - Retorna código de éxito/error para que la UI reaccione
CREATE OR ALTER PROCEDURE dbo.sp_InsertarEmpleado
    @Nombre  VARCHAR(128),
    @Salario MONEY
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @CantidadExistente INT;

    BEGIN TRY
        SELECT
            @CantidadExistente = COUNT(*)
        FROM
            dbo.Empleado AS e
        WHERE
            e.Nombre = @Nombre;

        IF @CantidadExistente > 0
        BEGIN
            SELECT
                50001                          AS CodigoError,
                'Nombre de Empleado ya existe.' AS Mensaje;

            RETURN;
        END

        INSERT INTO dbo.Empleado (Nombre, Salario)
        VALUES (@Nombre, @Salario);

        SELECT
            0                    AS CodigoError,
            'Inserción exitosa.' AS Mensaje;
    END TRY
    BEGIN CATCH
        SELECT
            ERROR_NUMBER()  AS CodigoError,
            ERROR_MESSAGE() AS Mensaje;
    END CATCH

    SET NOCOUNT OFF;
END
GO