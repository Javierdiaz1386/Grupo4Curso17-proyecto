import pymongo
import certifi
import json
from typing import Generic, TypeVar, get_args
from bson import ObjectId, DBRef

T = TypeVar('T')


class InterfaceRepository(Generic[T]):
    def __init__(self):
        ca = certifi.where()
        data_config = self.load_file_config()
        client = pymongo.MongoClient(
            "mongodb+srv://teamJavi:MisionTIC_2022@registraduriac17g4.5e5fdau.mongodb.net/"
            "registraduria_db?retryWrites=true&w=majority",
            tlsCAFile=ca
        )
        self.data_base = client['registraduria_db']
        model_class = get_args(self.__orig_bases__[0])
        self.collection = model_class[0].__name__.lower()

    def load_file_config(self) -> dict:
        with open("config.json") as file:
            data = json.load(file)
        return data

    def find_all(self) -> list:
        current_collection = self.data_base[self.collection]
        dataset = []
        for document in current_collection.find():
            document['_id'] = document['_id'].__str__()
            #document = self.transform_object_lds(document)
            document = self.get_values_db_ref(document)
            dataset.append(document)
        return dataset

    def find_by_id(self, id_: str) -> dict:
        current_collection = self.data_base[self.collection]
        document = current_collection.find_one({'_id': ObjectId(id_)})
        document = self.get_values_db_ref(document)
        if document:
            document['_id'] = document['_id'].__str__()
        else:
            document = {}
        return document

    def save(self, item: T) -> T:
        current_collection = self.data_base[self.collection]
        # TODO agregar esta wea (item = self.transform_refs(item)) cuando este listo esa funcion
        if hasattr(item, '_id') and item._id != "":
            id_ = item._id
            _id = ObjectId(id_)
            delattr(item, '_id')
            item = item.__dict__
            update_item = {"$set": item}
            document = current_collection.update_one({'_id': _id}, update_item)
        else:
            _id = current_collection.insert_one(item.__dict__)
            id_ = _id.inserted_id.__str__()
        document = current_collection.find_one({'_id': ObjectId(id_)})
        document['_id'] = document['_id'].__str__()
        return document

    def update(self, id_: str, item: T) -> T:
        current_collection = self.data_base[self.collection]
        _id = ObjectId(id_)
        delattr(item, '_id')
        item = item.__dict__
        update_item = {"$set": item}
        document = current_collection.update_one({'_id': _id}, update_item)
        return {"updated_count": document.matched_count}

    def delete(self, id_: str) -> dict:
        current_collection = self.data_base[self.collection]
        _id = ObjectId(id_)
        result = current_collection.delete_one({'_id': _id})
        return {"delete_count": result.deleted_count}

    def query(self, query: dict) -> list:
        current_collection = self.data_base[self.collection]
        dataset = []
        for document in current_collection.find(query):
            document['id_'] = document['id_'].__str__()
            document = self.transform_object_lds(document)
            document = self.get_values_db_ref(document)
            dataset.append(document)
        return dataset

    def query_aggregation(self, query: dict) -> list:
        current_collection = self.data_base[self.collection]
        dataset = []
        for document in current_collection.aggregate(query):
            document['id_'] = document['id_'].__str__()
            document = self.transform_object_lds(document)
            document = self.get_values_db_ref(document)
            dataset.append(document)
        return dataset

    def get_values_db_ref(self, document):
        keys = document.keys()
        for key in keys:
            if isinstance(document.get(key), DBRef):
                collection_ = self.data_base[document[key].collection]
                value = collection_.find_one({'_id': ObjectId(document[key].id)})
                value['_id'] = value['_id'].__str__()
                document[key] = value
                document[key] = self.get_values_db_ref(document[key])
            elif isinstance(document.get(key), list) and len(document.get(key)) > 0:
                document[key] = self.get_values_db_ref_from_list(document[key])
            elif isinstance(document.get(key), dict):
                document[key] = self.get_values_db_ref(document[key])
        return document

    def get_values_db_ref_from_list(self):
        pass

    def transform_object_lds(self):
        pass

    def transform_refs(self):
        pass

    def format_list(self):
        pass

    def object_to_db_ref(self):
        pass
