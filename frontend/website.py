from flask import Flask, render_template, request, redirect, url_for
import os
import pyodbc
from dotenv import load_dotenv

#para cargar las variables de entorno desde el archivo .env
load_dotenv()

#Se decidió trabajar con flask para crear la página web
app = Flask(__name__)

# Datos de conexión (vienen del archivo .env, no se escriben directo acá)
DB_SERVER = os.getenv("DB_SERVER")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = "BD_Empleados"

#Para definir los parametros de la conexion a la base de datos se necesita el archivo .env bien configurado con los datos de conexión a la base de datos.
def obtener_conexion():
    """Abre una conexión nueva a SQL Server."""
    cadena_conexion = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={DB_SERVER},1433;"
        f"DATABASE={DB_NAME};"
        f"UID={DB_USER};"
        f"PWD={DB_PASSWORD};"
        f"TrustServerCertificate=yes;"
    )
    return pyodbc.connect(cadena_conexion)


def obtener_empleados(): # Obtiene la lista de empleados desde la base de datos utilizando el stored procedure sp_ObtenerEmpleados
    """Llama a sp_ObtenerEmpleados y devuelve una lista de diccionarios."""
    conexion = obtener_conexion()
    try:
        cursor = conexion.cursor()
        cursor.execute("{CALL sp_ObtenerEmpleados}")

        columnas = [columna[0] for columna in cursor.description]
        filas = cursor.fetchall()

        return [dict(zip(columnas, fila)) for fila in filas]
    finally:
        conexion.close()


def insertar_empleado(nombre, salario): #Envia los datos del nuevo empleado a la base de datos utilizando el stored procedure sp_InsertarEmpleado y maneja el error en caso de que el nombre del empleado ya exista en la base de datos.
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
        

#Aquí se definen las rutas de la aplicación web
#"Llamada a la página 1 o principal, donde muestra tabla y boton"
@app.route("/")
def inicio():
    empleados = obtener_empleados()  # Obtener la lista de empleados a traves de la función obtener_empleados()
    return render_template("empleados.html", empleados=empleados)


#Llamada a la página 2 o insertar, donde esta el formulario para insertar un nuevo empleado
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # Procesar los datos del formulario
        nombre = request.form["nombre"]
        salario = request.form["salario"]

        try:
            salario_float = float(salario)
        except ValueError:
            return render_template("add.html", error="El salario debe ser un valor numérico válido.")

        codigo_error, mensaje = insertar_empleado(nombre, salario_float)

        if codigo_error == 0:
            # Inserción exitosa: volvemos a la página principal con el grid actualizado
            return redirect(url_for("inicio"))
        else:
            # codigo_error == 50001 -> nombre duplicado (u otro error del SP)
            return render_template("add.html", error=mensaje)

    return render_template("add.html", error=None)



# Ruta temporal para probar la pantalla de éxito
@app.route("/prueba-exito")
def prueba_exito():
    return render_template("exito.html")




# Ruta temporal para probar la pantalla de error
@app.route("/prueba-error")
def prueba_error():
    return render_template("error.html")


if __name__ == "__main__":
    app.run(debug=True)