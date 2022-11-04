from models.votoModel import Voto
from repositories.votoRepository import VotoRepository


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
        response = VotoRepository().find_all()
        print(response)
        return response

    def show(self, id_: str) -> list:
        """
        This method returns a 'Voto' according to the ID requested in the DB
        :param id_: voto id str
        :return: voto according id
        """
        response = VotoRepository().find_by_id(id_)
        voto = Voto(response)
        return voto.__dict__

    def create(self, voto_: dict) -> dict:
        """
        This method allows entering information of a 'Voto' to the BD
        :param voto_:
        :return: voto created
        """
        voto = Voto(voto_)

        return VotoRepository().save(voto)

    def update(self, id_: str, voto_: dict) -> dict:
        """
        This method allows updating information of a 'Voto' to the BD
        :param id_: Voto ID for update
        :param voto_:
        :return:
        """
        data = voto_
        data['_id'] = id_
        voto = Voto(data)
        return voto.__dict__

    def delete(self, id_: str) -> dict:
        """
        This method allows you to remove information of a 'Voto' to the BD
        :param id_:
        :return:
        """
        return {"Delete count": 1}
