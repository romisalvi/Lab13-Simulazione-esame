import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.g=nx.DiGraph()
        self.vertici=[]
        self.anno=None
        self.BP=[]
        self.lenMax=0
        self.idMap={}
        pass

    def getBP(self,state):
        parziale=[state]
        visitabili=self.getVisitabili(state,parziale)
        self.ricorsione(parziale,visitabili)
        return self.BP,self.lenMax

    def ricorsione(self,parziale,visitabili):
        print("r")
        x=len(parziale)
        if x > self.lenMax:
            self.lenMax=x
            self.BP=copy.deepcopy(parziale)
            print(x)
        for nodo in visitabili:
            parziale.append(nodo)
            newVis=self.getVisitabili(nodo,parziale)
            self.ricorsione(parziale,newVis)
            parziale.pop()
    def getVisitabili(self, state,parziale):
        vis=[]
        for nodo in self.g.successors(state):
            if nodo not in parziale:
                vis.append(nodo)
        return vis



    def getAnni(self):
        return DAO.getAnni()
    def creaGrafo(self, anno):
        self.g.clear()
        self.anno=anno
        self.g.add_nodes_from(DAO.getStati(anno))
        self.vertici=self.g.nodes
        for x in self.vertici:
            self.idMap[x.id]=x
        print(self.g)
        archi=DAO.getAvvistamenti(anno)
        for x in archi:

            self.g.add_edge(self.idMap[x[0].upper()],self.idMap[x[1].upper()])
        print(self.g)

    def getStates(self,anno):
        return DAO.getStati(anno)
    def getPeS(self,stato):
        pred=self.g.predecessors(stato)
        succ=self.g.successors(stato)
        return pred,succ

    def returnState(self,id): return self.idMap[id]


