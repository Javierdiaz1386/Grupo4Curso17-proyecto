from models.partidoModel import Partido


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
        data = {
            "_id": "1",
            "nombre": "Partido Liberal",
            "lema": "Oportunidades para todos"
        }
        partido = Partido(data)
        return [partido.__dict__]

    def show(self, id_: str) -> list:
        """
        This method returns a 'Partido' according to the ID requested in the DB
        :param id_:
        :return: partido ID
        """
        data = {
            "_id": id_,
            "nombre": "Partido Liberal",
            "lema": "Oportunidades para todos"
        }
        partido = Partido(data)
        return partido.__dict__

    def create(self, partido_: dict) -> dict:
        """
        This method allows entering information of a 'Partido' to the BD
        :param partido_:
        :return:
        """
        partido = Partido(partido_)
        return partido.__dict__

    def update(self, id_: str, partido_: dict) -> dict:
        """
        This method allows updating information of a 'Partido' to the BD
        :param id_:
        :param partido_:
        :return:
        """
        data = partido_
        data['_id'] = id_
        partido = Partido(data)
        return partido.__dict__

    def delete(self, id_: str) -> dict:
        """
        This method allows you to remove information of a 'Partido' to the BD
        :param id_:
        :return:
        """
        return {"Delete count": 1}
