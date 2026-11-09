from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_biblioteche(self):
        cnx = DBConnect.get_connection()
        query = "select * from biblioteca"
        cursor = cnx.cursor()
        cursor.execute(query)
        result = []
        for row in cursor:
            biblioteca = Biblioteca(*row)
            result.append(biblioteca)
        cursor.close()
        cnx.close()
        return result

    def get_nomi_biblioteche(self):
        cnx = DBConnect.get_connection()
        query = "select distinct id, nome from biblioteca"
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        cnx.close()
        return result

