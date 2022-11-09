from models.candidatoModel import Candidato
from repositories.candidatoRepository import CandidatoRepository


class CandidateController:

    def __init__(self):
        """
        This is the constructor of CandidateController class
        """
        print("Candidate Controller ready")

    def index(self) -> list:
        """
          This method returns all 'Candidate' persisted in the DB
        :param self
        :return: Candidate's list
        """
        response = CandidatoRepository().find_all()
        print(response)
        return response

    # Equivalent to 'one by id'
    def show(self, id_: str) -> list:
        """
         This method returns a 'Candidate' according to the ID requested in the DB
        :param id_: candidato id str
        :return: candidato according id
        """
        response = CandidatoRepository().find_by_id(id_)
        candidato = Candidato(response)
        return candidato.__dict__

    # Equivalent to 'insert'

    def create(self, candidate_: dict) -> dict:
        """
         This method allows entering information of a 'Candidate' to the BD
        :param candidate_:
        :return: candidato created
        """
        candidato = Candidato(candidate_)

        return CandidatoRepository().save(candidato)

    def update(self, id_, candidate_) -> dict:
        """

        This method allows updating information of a 'Candidate' to the BD
        :param id_: Candidato ID for update
        :param candidate_:
        :return:
        """
        response = CandidatoRepository().update(id_, candidate_)
        return response

    def delete(self, id_: str) -> dict:
        """
         This method allows you to remove information of a 'Candidate' to the BD
        :param id_:
        :return:
        """
        CandidatoRepository().delete(id_)
        return {"Delete count": 1}
