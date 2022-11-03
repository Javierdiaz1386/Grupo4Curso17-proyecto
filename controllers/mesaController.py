from models.mesaModel import Mesa


class MesaController:

    def __init__(self):
        """

        """
        print("Mesa Controller ready")

    def index(self) -> list:
        """

        :return:
        """
        print("return all mesas")

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("return one  mesa")

    def create(self, mesa_: dict) -> dict:
        """

        :param mesa_:
        :return:
        """
        print("insert a mesa")

    def update(self, id_: str, mesa_: dict) -> dict:
        """

        :param id_:
        :param mesa_:
        :return:
        """

        print("update a mesa")

    def delete(self, id_: str) -> str:
        """

        :param id_:
        :return:
        """
        print("delete a mesa")