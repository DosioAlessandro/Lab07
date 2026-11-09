import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_dropdown(self):
        self._view.dd_biblioteca.options.append(ft.DropdownOption(key="NULL", text="Nessun Filtro"))
        for i in Model().get_biblioteche():
            self._view.dd_biblioteca.options.append(ft.DropdownOption(key=f"{i["id"]}", text=f"{i["nome"]}"))
        self._view.dd_genere.options.append(ft.DropdownOption(key="NULL", text="Nessun Filtro"))
        for i in Model().get_generi():
            self._view.dd_genere.options.append(ft.dropdown.Option(f"{i["genere"]}"))

    # CALLBACKS DROPDOWN
    def seleziona_biblioteca(self,e):
        self.biblioteca_selezionata = self._view.dd_biblioteca.value
        return self.biblioteca_selezionata

    def seleziona_genere(self,e):
        self.genere_selezionato = self._view.dd_genere.value
        return self.genere_selezionato

    # AZIONE: MOSTRA LIBRI
    def handler_button(self):
        if self.biblioteca_selezionata is None or self.genere_selezionato is None:
            self._view.show_alert("Compilare i campi richiesti")
        else:
            lista_libri_scelti = Model().get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)
            if len(lista_libri_scelti) == 0:
                self._view.show_alert("Non ci sono libri che soddisfano la ricerca")
            else:
                self._view.list_view.controls.clear()
                for libro in lista_libri_scelti:
                    self._view.list_view.controls.append(ft.Text(str(libro)))