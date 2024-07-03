import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._year=None
        self._listYear = []
        self._listShape = []

    def fillDD(self):
        self._listYear=self._model.getYears()
        for x in self._listYear:
            self._view.ddyear.options.append(ft.dropdown.Option(x))
        self._view.update_page()
    def fillDDShape(self,e):
        self._year=self._view.ddyear.value
        self._listShape=self._model.getShapesxYear(self._year)
        self._view.ddshape.options.clear()
        for x in self._listShape:
            self._view.ddshape.options.append(ft.dropdown.Option(x))
        self._view.update_page()
    def fillDDState(self):
        listaStati=self._model.getStates()
        for s in listaStati:
            self._view.ddState.options.append(ft.dropdown.Option(text=s.id, key=s))
        self._view.update_page()



    def handle_graph(self, e):
        pass
    def handle_path(self, e):
        Stato=self._view.ddState.value
        print(Stato)
        pass