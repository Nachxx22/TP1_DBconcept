from flask import Flask, render_template, request 

#Se decidió trabajar con flask para crear la página web
app = Flask(__name__)

#Aquí se definen las rutas de la aplicación web

#"Llamada a la página 1 o principal, donde muestra tabla y boton"
@app.route("/")
def inicio():
    return render_template("empleados.html")


#Llamada a la página 2 o insertar, donde esta el formulario para insertar un nuevo empleado
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # Procesar los datos del formulario e imprimir para verificar que si se recibieron
        nombre = request.form["nombre"]
        salario = request.form["salario"]
        print("Nombre:", nombre)
        print("Salario:", salario)
    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)