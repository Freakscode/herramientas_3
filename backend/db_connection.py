from pymongo import MongoClient

"""Se crea una clase DBConnection con un método create_connection que se encarga de crear la conexión con la base de datos
y de los métodos para realizar operaciones CRUD en la base de datos.
"""
class DBConnection:
    def create_connection(self):
        client = MongoClient('localhost', 27017)
        db = client['test']
        return db
    
    ## Agrega métodos para insertar, actualizar y eliminar documentos en la base de datos.
    def insert_document(self, collection, document):
        db = self.create_connection()
        collection = db[collection]
        collection.insert_one(document)
        return ('Se inserto el documento')
    
    def update_document(self, collection, query, new_values):
        db = self.create_connection()
        collection = db[collection]
        collection.update_one(query, new_values)
        return ('Se actualizo el documento')
    
    def delete_document(self, collection, query):
        db = self.create_connection()
        collection = db[collection]
        collection.delete_one(query)
        return ('Se elimino el documento')
    
    ## Agrega un método para obtener todos los documentos de una colección.
    def get_documents(self, collection):
        db = self.create_connection()
        collection = db[collection]
        return collection.find()
    
    ## Agrega un método para obtener un documento por su id.
    def get_document_by_id(self, collection, id):
        db = self.create_connection()
        collection = db[collection]
        return collection
    
    ## Agrega un método para obtener documentos por un filtro.
    def get_documents_by_filter(self, collection, filter):
        db = self.create_connection()
        collection = db[collection]
        return collection.find(filter)
    
    ## Agrega un método para obtener documentos por un rango de fechas.
    def get_documents_by_date_range(self, collection, date_range):
        db = self.create_connection()
        collection = db[collection]
        return collection.find(date_range)    
    