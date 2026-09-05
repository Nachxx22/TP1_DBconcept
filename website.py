from flask import Flask

website = Flask(__name__)

@website.route("/")
def inicio():
    return "Proyecto 1 está funcionando correctamente"

if __name__ == "__main__":
    website.run(debug=True)