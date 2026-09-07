"""
Instalación previa (una sola vez):
    pip install flask pyodbc python-dotenv

Requiere tener instalado "ODBC Driver 17 for SQL Server" (u 18) en Windows.
Para verificar cuáles tenés disponibles, corré en una consola de Python:
    import pyodbc; print(pyodbc.drivers())
"""

import os
import pyodbc
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for

load_dotenv()

app = Flask(__name__)

DB_SERVER = os.getenv('DB_SERVER')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = 'BD_Empleados'


def obtener_conexion():
    """Abre una conexión nueva a SQL Server. Se cierra siempre en un finally."""
    cadena_conexion = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={DB_SERVER},1433;"
        f"DATABASE={DB_NAME};"
        f"UID={DB_USER};"
        f"PWD={DB_PASSWORD};"
        f"TrustServerCertificate=yes;"
    )
    return pyodbc.connect(cadena_conexion)


def obtener_empleados():
    """Llama a sp_ObtenerEmpleados y devuelve una lista de diccionarios."""
    conexion = obtener_conexion()
    try:
        cursor = conexion.cursor()
        cursor.execute("{CALL sp_ObtenerEmpleados}")

        columnas = [columna[0] for columna in cursor.description]
        filas = cursor.fetchall()

        empleados = [dict(zip(columnas, fila)) for fila in filas]
        return empleados
    finally:
        conexion.close()


def insertar_empleado(nombre, salario):
    """Llama a sp_InsertarEmpleado y devuelve (codigo_error, mensaje)."""
    conexion = obtener_conexion()
    try:
        cursor = conexion.cursor()
        cursor.execute("{CALL sp_InsertarEmpleado (?, ?)}", nombre, salario)

        fila = cursor.fetchone()
        codigo_error = fila[0]
        mensaje = fila[1]

        conexion.commit()
        return codigo_error, mensaje
    finally:
        conexion.close()

# Rutas

@app.route('/')
def index():
    empleados = obtener_empleados()
    return render_template('index.html', empleados=empleados)


@app.route('/add', methods=['GET'])
def add_get():
    return render_template('add.html', error=None)


@app.route('/add', methods=['POST'])
def add_post():
    nombre = request.form.get('nombre')
    salario = request.form.get('salario')

    try:
        salario_float = float(salario)
    except (TypeError, ValueError):
        return render_template('add.html', error='El salario debe ser un valor numérico válido.')

    codigo_error, mensaje = insertar_empleado(nombre, salario_float)

    if codigo_error == 0:
        return redirect(url_for('index'))
    else:
        # codigo_error == 50001 -> nombre duplicado (u otro error del SP)
        return render_template('add.html', error=mensaje)


if __name__ == '__main__':
    app.run(debug=True)