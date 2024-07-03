import flet as ft

from model.State import State


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listShape = []
        self.a=None

    def fillDD(self):
        anniAvv=self._model.getAnni()
        for x in anniAvv:
            self._view.ddyear.options.append(ft.dropdown.Option(str(x[0])+"/"+str(x[1])))
        pass

    def handle_graph(self, e):
        self.a=self._view.ddyear.value.split("/")[0]
        if self.a=="" or self.a is None:
            self._view.create_alert("Prima selezionare un anno!")
            self._view.update_page()
            return
        self._model.creaGrafo(self.a)
        self.fillDDstate(self.a)

        pass
    def fillDDstate(self,anno):
        listaStati=self._model.getStates(anno)
        for x in listaStati:
            self._view.ddstate.options.append(ft.dropdown.Option(x.id))
        self._view.update_page()

    def handle_path(self, e):
        stato=self._model.returnState(self._view.ddstate.value)
        BP,lenMax=self._model.getBP(stato)
        if lenMax==1:
            self._view.txtOut2.controls.append(ft.Text(f"Nessun percorso trovato, sorry"))
            self._view.update_page()
            return
        self._view.txtOut2.controls.clear()
        self._view.txtOut2.controls.append(ft.Text(f"Trovato percorso con {lenMax-1} archi "))
        for x in BP:
            self._view.txtOut2.controls.append(ft.Text(f"{x.id} "))
        self._view.update_page()



        pass
    def handleS(self,e):
        self._view.txt_result.controls.clear()
        stato=self._model.returnState(self._view.ddstate.value)


        self._view.txt_result.controls.append(ft.Text(f"Grafo correttamente creato con "
                                                      f" nodi e"
                                                      f"  archi."
                                                      f"Stato selezionato: {stato.id}"))
        pred,succ=self._model.getPeS(stato)
        self._view.txt_result.controls.append(ft.Text(f" predecessori:"))
        for x in pred:
            self._view.txt_result.controls.append(ft.Text(f"{x.id}"))
        self._view.txt_result.controls.append(ft.Text(f" successori:"))
        for x in succ:
            self._view.txt_result.controls.append(ft.Text(f"{x.id}"))
        self._view.update_page()


