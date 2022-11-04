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
        data = {
            "_id": "1",
            "numero_mesa": "1",
            "cantidad_inscritos": "30"
        }
        mesa = Mesa(data)
        return [mesa.__dict__]

    def show(self, id_: str) -> list:
        """

        :param id_:
        :return:
        """
        data = {
            "_id": "1",
            "numero_mesa": "1",
            "cantidad_inscritos": "30"
        }
        mesa = Mesa(data)
        return mesa.__dict__

    def create(self, mesa_: dict) -> dict:
        """

        :param mesa_:
        :return:
        """
        mesa = Mesa(mesa_)
        return mesa.__dict__

    def update(self, id_: str, mesa_: dict) -> dict:
        """

        :param id_:
        :param mesa_:
        :return:
        """

        data = mesa_
        data['_id'] = id_
        mesa = Mesa(data)
        return mesa.__dict__

    def delete(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        return {"Delete count": 1}