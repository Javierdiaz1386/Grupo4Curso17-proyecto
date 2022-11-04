from flask import Blueprint
from flask import request

from controllers.candidatoController import  CandidatoController

candidato_blueprints = Blueprint('candidato_blueprint', __name__)
candidato_controller = CandidatoController()


@candidato_blueprints.route("/candidato/all", methods=['GET'])
def get_candidato():
    response = candidato_controller.index(),
    return response, 200


@candidato_blueprints.route("/candidato/<string:id_>", methods=['GET'])
def get_candidato_by_id(id_):
    response = candidato_controller.show(id_),
    return response, 200


@candidato_blueprints.route("/candidato/insert", methods=['POST'])
def insert_candidato():
    candidato = request.get_json()
    response = candidato_controller.create(candidato)
    return response, 201


@candidato_blueprints.route("/candidato/update/<string:id_>", methods=['PATCH'])
def update_candidato(id_):
    candidato = request.get_json()
    response = candidato_controller.update(id_, candidato)
    return response, 201


@candidato_blueprints.route("/candidato/delete/<string: id_>", methods=['DELETE'])
def delete_candidato(id_):
    response = candidato_controller.delete(id_)
    return response, 204
