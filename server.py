from flask import Flask
from flask_cors import CORS, cross_origin
from lisls import jog


app = Flask(__name__)
CORS(app)

@app.route("/teste")
def teste():
    return {"teste":["teste","teste"]}


@app.route("/jogador")
def jogador():
    resultado =jog()
    return resultado

if __name__ == "__main__":
    app.run(debug=True)