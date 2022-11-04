from models.candidate import Candidate


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
        print("return all candidates")
        data = {
            "cedula": "1232434",
            "numero_resolucion": "9",
            "nombre": "Pedro",
            "apellido": "Martinez"
        }
        candidate = Candidate(data)
        return [candidate.__dict__]

    # Equivalent to 'one by id'
    def show(self, id_) -> dict:
        """

         This method returns a 'Candidate' according to the ID requested in the DB
        :param id_:
        :return:
        """
        print("return one candidate")
        data = {
             "_id": id_,
             "cedula": "1232434",
             "numero_resolucion": "9",
             "nombre": "Pedro",
             "apellido": "Martinez"
        }
        student = Candidate(data)
        return candidate.__dict__

    # Equivalent to 'insert'
    def create(self, candidate_) -> dict:
        """
         This method allows entering information of a 'Candidate' to the BD
        :param candidate_:
        :return:
        """
        print("insert a candidate")
        candidate = Candidate(candidate_)
        return candidate.__dict__

    def update(self, id_, candidate_) -> dict:
        """
        
        This method allows updating information of a 'Candidate' to the BD
        :param id_:
        :param candidate_:
        :return:
        """
        print("update a candidate")
        data = candidate_
        data["_id"] = id_
        candidate = Candidate(data)
        return candidate.__dict__

    def delete(self, id_) -> dict:
        """
         This method allows you to remove information of a 'Candidate' to the BD
        :param id_:
        :return:
        """
        print("Delete count" + id_)
        return {
            "Delete count": 1
        }
