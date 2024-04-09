from db_connection import DBConnection

## Se hereda de la clase DBConnection para poder utilizar los métodos de la clase padre.

class DBMethods(DBConnection):
    def __init__(self):
        super().__init__()
