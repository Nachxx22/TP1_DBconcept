from flask import Flask, render_template, request 
#Se decidió trabajar con flask para crear la página web
app = Flask(__name__)



#Aquí se definen las rutas de la aplicación web
#"Llamada a la página 1 o principal, donde muestra tabla y boton"
@app.route("/")
def inicio():
    empleados = [
        [1, "Juan Pérez", 2500],
        [2, "María Gómez", 3000],
        [3, "Carlos Rodríguez", 2800]
    ]
    return render_template("empleados.html", empleados=empleados)




#Llamada a la página 2 o insertar, donde esta el formulario para insertar un nuevo empleado
@app.route("/add", methods=["GET", "POST"])
def add():
    #Si el método es POST, significa que se envió el formulario, entonces se procesan los datos
    if request.method == "POST":s
        nombre = request.form["nombre"]
        salario = request.form["salario"]
        print("Nombre:", nombre)
        print("Salario:", salario)
    return render_template("add.html")



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