from flask import Blueprint
from flask import request

from controllers.partidoController import PartidoController

partido_blueprint = Blueprint('partido_blueprint', __name__)
partido_controller = PartidoController()


@partido_blueprint.route("/partido/all", methods=['GET'])
def get_partidos():
    response = partido_controller.index()
    return response, 200


@partido_blueprint.route("/partido/<string:id_>", methods=['GET'])
def get_partido_by_id(id_):
    response = partido_controller.show(id_)
    return response, 200


@partido_blueprint.route("/partido/insert", methods=['POST'])
def insert_partido():
    partido = request.get_json()
    response = partido_controller.create(partido)
    return response, 201


@partido_blueprint.route("/partido/update/<string:id_>", methods=['PATCH'])
def update_partido(id_):
    partido = request.get_json()
    response = partido_controller.update(id_, partido)
    return response, 201


@partido_blueprint.route("/partido/delete/<string:id_>", methods=['DELETE'])
def delete_partido(id_):
    response = partido_controller.delete(id_)
    return response, 204
