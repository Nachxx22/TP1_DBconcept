// Dos funciones independientes para probar cada stored procedure por separado
// Cada una abre su propia conexión y la cierra al terminar


// Uso:
//   node sps.js listar
//   node sps.js insertar "Nombre Apellido" 250000.00

// Configuración del entorno
require('dotenv').config();
const sql = require('mssql');

const config = {
    server: process.env.DB_SERVER,
    port: 1433,
    database: 'BD_Empleados',
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    options: {
        encrypt: false,
        trustServerCertificate: true
    }
};

// SP 1: sp_ObtenerEmpleados
async function ObtenerEmpleados() {
    let pool;
    try {
        console.log('--- Probando sp_ObtenerEmpleados ---');
        pool = await sql.connect(config);

        const resultado = await pool.request().execute('sp_ObtenerEmpleados');

        console.log(`Se recibieron ${resultado.recordset.length} filas:`);
        console.table(resultado.recordset);
    } catch (error) {
        console.error('Error en sp_ObtenerEmpleados:', error.message);
    } finally {
        if (pool) await pool.close();
    }
}


// SP 2: sp_InsertarEmpleado
async function InsertarEmpleado(nombre, salario) {
    let pool;
    try {
        console.log('--- Probando sp_InsertarEmpleado ---');
        console.log(`Nombre: ${nombre} | Salario: ${salario}`);

        pool = await sql.connect(config);

        const resultado = await pool.request()
            .input('Nombre', sql.VarChar(128), nombre)
            .input('Salario', sql.Money, salario)
            .execute('sp_InsertarEmpleado');

        console.log('Resultado del SP:');
        console.table(resultado.recordset);
    } catch (error) {
        console.error('Error en sp_InsertarEmpleado:', error.message);
    } finally {
        if (pool) await pool.close();
    }
}


// Selección según el argumento recibido por la consola
const comando = process.argv[2];

if (comando === 'listar') {
    ObtenerEmpleados();
} else if (comando === 'insertar') {
    const nombre = process.argv[3];
    const salario = parseFloat(process.argv[4]);

    if (!nombre || isNaN(salario)) {
        console.error('Uso: node sps.js insertar "Nombre Apellido" 250000.00');
    } else {
        InsertarEmpleado(nombre, salario);
    }
} else {
    console.log('Uso:');
    console.log('node sps.js listar');
    console.log('node sps.js insertar "Nombre Apellido" 250000.00');
}