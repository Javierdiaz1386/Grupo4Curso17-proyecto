from models.partidoModel import Partido


class PartidoController:

    def __init__(self):
        print("Partido Controller ready")

    # GET con toda la información de la tabla
    def index(self) -> list:
        print("All Partido")
        data = {
            "_id": "1",
            "nombre": "Partido Liberal",
            "lema": "Oportunidades para todos"
        }
        partido = Partido(data)
        return [partido.__dict__]

    # GET con la información de un solo partido de la tabla
    def show(self, id_: str) -> list:
        print("Return one Partido")
        data = {
            "_id": id_,
            "nombre": "Partido Liberal",
            "lema": "Oportunidades para todos"
        }
        partido = Partido(data)
        return partido.__dict__

    # POST para ingresar información a la tabla
    def create(self, partido_: dict) -> dict:
        print("Insert an Partido")
        partido = Partido(partido_)
        return partido.__dict__

    # UPDATE para actualizar información de la tabla
    def update(self, id_: str, partido_: dict) -> dict:
        print("Update an Partido")
        data = partido_
        data['_id'] = id_
        partido = Partido(data)
        return partido.__dict__

    # DELETE para eliminar información de la tabla
    def delete(self, id_: str) -> dict:
        print("Delete an Partido " + id_)
        return {"Delete count": 1}