from flask import Blueprint
from flask import request

from controllers.partidoController import PartidoController

partido_blueprint = Blueprint('partido_blueprint', __name__)
partido_controller = PartidoController()


@partido_blueprint.route("/partido/all", methods=['GET'])
def get_partidos():
    response = partido_controller.index();
    return response, 200