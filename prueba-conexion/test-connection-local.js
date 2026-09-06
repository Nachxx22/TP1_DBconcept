//configuracion del env
require('dotenv').config();
// Prueba de conexión a SQL Server 2022 local(Tailscale)
// Instalación previa (una sola vez):
//   npm init -y
//   npm install mssql

const sql = require('mssql');

// Si es instancia default: server = '100.x.x.x' (IP de Tailscale de la máquina host(Nacho Desktop))
// Si es instancia nombrada (ej. SQLEXPRESS) en este caso: server = '100.xx.xx.xx\\SQLEXPRESS' (de esta manera no funciona)
const config = {
    server: process.env.DB_SERVER
    ,
    port: 1433,
    database: 'BD_Empleados',
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    options: {
        encrypt: false,             // no es necesario en red local/Tailscale (Para la nube si)
        trustServerCertificate: true // evita error de certificado autofirmado en local
    }
};


// Probar la conexión con la base de datos y el Storeprocedure sp_ObtenerEmpleados
async function probarConexion() {
    try {
        console.log('Conectando a SQL Server local...');
        const pool = await sql.connect(config);
        console.log('Conexión exitosa.');

        console.log('Ejecutando sp_ObtenerEmpleados...');
        const resultado = await pool.request().execute('sp_ObtenerEmpleados'); // Ejecuta el procedimiento almacenado

        console.log(`Se recibieron ${resultado.recordset.length} filas:`);
        console.table(resultado.recordset);

        await pool.close();
    } catch (error) {
        console.error('Error de conexión o ejecución:', error.message); // para obtener el mensaje de error y una pequeña descripcion de que sucedio
    }
}

probarConexion();