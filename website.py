from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Proyecto Base de Datos funcionando"

if __name__ == "__main__":
    app.run(debug=True)