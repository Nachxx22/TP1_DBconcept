from flask import Flask, render_template

app = Flask(__name__)

"Aquí se definen las rutas de la aplicación web"

"Llamada a la página 1 o principal, donde muestra tabla y boton"
@app.route("/")
def inicio():
    return render_template("empleados.html")


"Llamada a la página 2 o insertar, donde esta el formulario para insertar un nuevo empleado"
@app.route("/add")
def add():
    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)