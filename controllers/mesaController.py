from models.mesaModel import Mesa


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
        data = {
            "_id": "1",
            "numero_mesa": "1",
            "cantidad_inscritos": "30"
        }
        mesa = Mesa(data)
        return [mesa.__dict__]

    def show(self, id_: str) -> list:
        """
        This method returns a 'Mesa' according to the ID requested in the DB
        :param id_:
        :return:
        """
        data = {
            "_id": id_,
            "numero_mesa": "1",
            "cantidad_inscritos": "30"
        }
        mesa = Mesa(data)
        return mesa.__dict__

    def create(self, mesa_: dict) -> dict:
        """
        This method allows entering information of a 'Mesa' to the BD
        :param mesa_:
        :return:
        """
        print("insert a Mesa")
        mesa = Mesa(mesa_)
        return mesa.__dict__

    def update(self, id_: str, mesa_: dict) -> dict:
        """
        This method allows updating information of a 'Mesa' to the BD
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
        This method allows you to remove information of a 'Mesa' to the BD
        :param id_:
        :return:
        """
        return {"Delete count": 1}