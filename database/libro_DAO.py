from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_libro(self):
        cnx = DBConnect.get_connection()
        query = ("select l.*, b.nome"
                 "from libro l, biblioteca b "
                 "where l.id_biblioteca = b.id ")
        cursor = cnx.cursor()
        cursor.execute(query)
        result = []
        for row in cursor:
            libro = Libro(*row)
            result.append(libro)
        cursor.close()
        cnx.close()
        return result

    def get_genere_libri(self):
        cnx = DBConnect.get_connection()
        query = "select distinct genere from libro"
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        cnx.close()
        return result

    def get_libri_filtrati(self, biblioteca, genere):
        cnx = DBConnect.get_connection()
        if genere != "NULL":
            genere = f'"{genere}"'
        query =f''' select l.*, b.nome 
                from libro l, biblioteca b 
                where l.id_biblioteca = b.id and b.id = coalesce({biblioteca},b.id) and l.genere = coalesce({genere}, l.genere) 
                '''
        cursor = cnx.cursor()
        cursor.execute(query)
        result = []
        for row in cursor:
            libro = Libro(*row)
            result.append(libro)
        cursor.close()
        cnx.close()
        return result
