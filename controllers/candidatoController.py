from models.candidato import Candidato


class CandidatoController:

    def __init__(self):
        """
        Este es el constructor de la clase CandidatoController
        """
        print("Controlador candidato listo")

    def index(self) -> list:
        """
        Este método retorna todos los candidatos disponibles en la db
        :param self
        :return:
        """
        print("retorna todos los candidatos")
        data = {
            "cedula": "1232434",
            "numero_resolucion": "9",
            "nombre": "Pedro",
            "apellido": "Martinez"
        }
        candidato = Candidato(data)
        return [candidato.__dict__]

    # Equivalent to 'one by id'
    def show(self, id_) -> dict:
        """

        Este método retorna un candidato específico en la db
        :param id_:
        :return:
        """
        print("retorna un estudiante")
        data = {
             "_id": id_,
             "cedula": "1232434",
             "numero_resolucion": "9",
             "nombre": "Pedro",
             "apellido": "Martinez"
        }
        student = Candidato(data)
        return candidato.__dict__

    # Equivalent to 'insert'
    def create(self, candidato_) -> dict:
        """
        Este método inserta un candidato específico en la db
        :param candidato_:
        :return:
        """
        print("inserte un candidato")
        candidato = Candidato(candidato_)
        return candidato.__dict__

    def update(self, id_, candidato_) -> dict:
        """
        Este método actualiza un candidato específico en la db
        :param id_:
        :param candidato_:
        :return:
        """
        print("actualización un candidato")
        data = candidato_
        data["_id"] = id_
        candidato = Candidato(data)
        return candidato.__dict__

    def delete(self, id_) -> dict:
        """
        Este método elimina un candidato específico en la db
        :param id_:
        :return:
        """
        print("eliminación de candidato" + id_)
        return {
            "candidato eliminado": 1
        }
