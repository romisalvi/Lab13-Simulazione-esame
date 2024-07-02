import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listShape = []
        self.s=None
        self.y=None

    def fillDD(self):
        self._listShape,self._listYear=self._model.getShapesnYears()
        for el in self._listYear:
            self._view.ddyear.options.append(ft.dropdown.Option(el))
        for el in self._listShape:
            self._view.ddshape.options.append(ft.dropdown.Option(el))
        pass

    def handle_graph(self, e):
        self._view.txt_result.controls.clear()
        self.s=self._view.ddshape.value
        self.y=self._view.ddyear.value
        if self.s is None:
            self._view.create_alert("Selezionare una forma")
            self._view.update_page()
            return
        if self.y is None:
            self._view.create_alert("Selezionare un anno")
            self._view.update_page()
            return
        n,a=self._model.creaGrafo(self.s,self.y)
        self._view.txt_result.controls.append(ft.Text(f"Nodi:{n}, archi:{a}"))
        lista=self._model.getPesi()
        for x in lista:
            self._view.txt_result.controls.append(ft.Text(f"{x}"))
        self._view.update_page()

        pass
    def handle_path(self, e):
        self._view.txtOut2.controls.clear()

        if len(self._model.g.nodes)==0:
            self._view.create_alert("Creare ìl grafo")
            self._view.update_page()
            return
        pesoMax=self._model.getBP()
        self._view.txtOut2.controls.append(ft.Text(f"Percorso di distanza {pesoMax}"))
        lista=self._model.getLista()
        for x in lista:
            self._view.txtOut2.controls.append(ft.Text(f"{x}"))
        self._view.update_page()

        pass
