from models.partidoModel import Partido
from repositories.partidoRepository import PartidoRepository


class PartidoController:

    def __init__(self):
        """
        This is the constructor of PartidoController class
        """
        print("Partido Controller ready")

    def index(self) -> list:
        """
        This method returns all 'Partido' persisted in the DB
        :return: partido's list
        """
        response = PartidoRepository().find_all()
        print(response)
        return response

    def show(self, id_: str) -> list:
        """
        This method returns a 'Partido' according to the ID requested in the DB
        :param id_:
        :return: partido ID
        """
        response = PartidoRepository().find_by_id(id_)
        partido = Partido(response)
        return partido.__dict__

    def create(self, partido_: dict) -> dict:
        """
        This method allows entering information of a 'Partido' to the BD
        :param partido_:
        :return:
        """
        print("insert a 'Partido'")
        partido = Partido(partido_)
        return PartidoRepository().save(partido)

    def update(self, id_: str, partido_: dict) -> dict:
        """
        This method allows updating information of a 'Partido' to the BD
        :param id_:
        :param partido_:
        :return:
        """
        response = PartidoRepository().update(id_, partido_)
        return response

    def delete(self, id_: str) -> dict:
        """
        This method allows you to remove information of a 'Partido' to the BD
        :param id_:
        :return:
        """
        PartidoRepository().delete(id_)
        return {"Delete count": 1}
