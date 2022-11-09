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

        return response
    # Equivalent to 'one by id'
    def show(self, id_) -> dict:
        """

         This method returns a 'Candidate' according to the ID requested in the DB
        :param id_:
        :return:
        """
        pass
    # Equivalent to 'insert'

    def create(self, candidate_) -> dict:
        """
         This method allows entering information of a 'Candidate' to the BD
        :param candidate_:
        :return:
        """
        pass

    def update(self, id_, candidate_) -> dict:
        """
        
        This method allows updating information of a 'Candidate' to the BD
        :param id_:
        :param candidate_:
        :return:
        """
        pass

    def delete(self, id_) -> dict:
        """
         This method allows you to remove information of a 'Candidate' to the BD
        :param id_:
        :return:
        """
        pass