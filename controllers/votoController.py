from models.votoModel import Voto


class VotoController:

    def __init__(self):
        """
        This is the constructor of VotoController class
        """
        print("Voto Controller ready")

    def index(self) -> list:
        """
        This method returns all 'Voto' persisted in the DB
        :return: voto's list
        """
        data = {
            "_id": "1",
            "numero_mesa": "4",
            "id_partido": "9"
        }
        voto = VotoModel(data)
        return [voto.__dict__]

    def show(self, id_: str) -> list:
        """
        This method returns a 'Voto' according to the ID requested in the DB
        :param id_: voto id str
        :return: voto according id
        """
        data = {
            "_id": id_,
            "numero_mesa": "50",
            "id_partido": "5"
        }
        voto = VotoModel(data)
        return voto.__dict__

    def create(self, voto_: dict) -> dict:
        """
        This method allows entering information of a 'Voto' to the BD
        :param voto_:
        :return: voto created
        """
        voto = VotoModel(voto_)
        return voto.__dict__

    def update(self, id_: str, voto_: dict) -> dict:
        """
        This method allows updating information of a 'Voto' to the BD
        :param id_: Voto ID for update
        :param voto_:
        :return:
        """
        data = voto_
        data['_id'] = id_
        voto = VotoModel(data)
        return voto.__dict__

    def delete(self, id_: str) -> dict:
        """
        This method allows you to remove information of a 'Voto' to the BD
        :param id_:
        :return:
        """
        return {"Delete count": 1}
