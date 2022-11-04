from flask import Flask
from flask import jsonify
from flask_cors import CORS
import json
from waitress import serve

from blueprints.candidatoBlueprint import candidate_blueprint
from blueprints.mesaBlueprint import mesa_blueprints
from blueprints.partidoBlueprint import partido_blueprint
from blueprints.votoBlueprint import voto_blueprint

app = Flask(__name__)
cors = CORS(app)
app.register_blueprint(candidate_blueprint)
app.register_blueprint(mesa_blueprints)
app.register_blueprint(partido_blueprint)
app.register_blueprint(voto_blueprint)


@app.route("/", methods=['GET'])
def home():
    response = {"message": "Server running ..."}
    return jsonify(response)


def load_file_config():
    with open("config.json") as file:
        data = json.load(file)
    return data


if __name__ == '__main__':
    dataConfig = load_file_config()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
