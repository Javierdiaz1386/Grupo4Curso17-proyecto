from flask import Blueprint
from flask import request

from controllers.votoController import VotoController

voto_blueprint = Blueprint('partido_blueprint', __name__)
voto_controller = VotoController()


@voto_blueprint.route("/voto/all", methods=['GET'])
def get_voto():
    response = voto_controller.index();
    return response, 200


@voto_blueprint.route("/voto/<string:id_>", methods=['GET'])
def get_voto_by_id(id_):
    response = voto_controller.show(id_)
    return response, 200


@voto_blueprint.route("/voto/insert", methods=['POST'])
def insert_voto():
    voto = request.get_json()
    response = voto_controller.create(voto)
    return response, 201


@voto_blueprint.route("/voto/update/<string:id_>", methods=['PATCH'])
def update_voto(id_):
    voto = request.get_json()
    response = voto_controller.update(id_, voto)
    return response, 201


@voto_blueprint.route("/voto/delete/<string:id_>", methods=['DELETE'])
def delete_voto(id_):
    response = voto_controller.delete(id_)
    return response, 204
