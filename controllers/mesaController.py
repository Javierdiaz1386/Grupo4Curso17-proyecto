from models.mesaModel import Mesa
from repositories.mesaRepository import MesaRepository


class MesaController:

    def __init__(self):
        """
        This is the constructor of MesaController class
        """
        print("Mesa Controller ready")

    def index(self) -> list:
        """
        This method returns all 'Mesa' persisted in the DB
        :return:
        """
        response = MesaRepository().find_all()
        print(response)
        return response

    def show(self, id_: str) -> list:
        """
        This method returns a 'Mesa' according to the ID requested in the DB
        :param id_:
        :return:
        """
        response = MesaRepository().find_by_id(id_)
        mesa = Mesa(response)
        return mesa.__dict__

    def create(self, mesa_: dict) -> dict:
        """
        This method allows entering information of a 'Mesa' to the BD
        :param mesa_:
        :return:
        """
        mesa = Mesa(mesa_)
        return MesaRepository().save(mesa)

    def update(self, id_: str, mesa_: dict) -> dict:
        """
        This method allows updating information of a 'Mesa' to the BD
        :param id_:
        :param mesa_:
        :return:
        """

        response = MesaRepository().update(id_, mesa_)
        return response

    def delete(self, id_: str) -> dict:
        """
        This method allows you to remove information of a 'Mesa' to the BD
        :param id_:
        :return:
        """
        MesaRepository().delete(id_)
        return {"Delete count": 1}