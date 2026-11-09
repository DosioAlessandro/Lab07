from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

        self._lista_biblioteche = None
        self._lista_generi = None

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        libri = self._libro_dao.get_libri_filtrati(biblioteca, genere)
        return libri


    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        self._lista_generi = self._libro_dao.get_genere_libri()
        return self._lista_generi

    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        self._lista_biblioteche = self._biblioteca_dao.get_nomi_biblioteche()
        return self._lista_biblioteche




