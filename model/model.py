import copy

import geopy
import networkx as nx

from database.DAO import DAO
from geopy.distance import distance


class Model:
    def __init__(self):
        self.g=nx.Graph()
        self.confini=DAO.getConfini()
        self.BP=[]
        self.pesoMax=0
    def getShapesnYears(self):
        shapes=DAO.getShapes()
        years=DAO.getYears()
        return shapes,years
    def creaGrafo(self,shape,year):
        self.g.clear()

        self.g.add_nodes_from(DAO.getStatiePeso(shape,year))
        for x in self.g.nodes:
            for y in self.g.nodes:
                if x.id<y.id and (x.id,y.id) in self.confini:
                    if x.Sightings+y.Sightings==0:
                        print ("X")
                    self.g.add_edge(x,y,weight=x.Sightings+y.Sightings)
        print(self.g)
        return len(self.g.nodes), len(self.g.edges)
    def getPesi(self):
        lista=[]
        for n in self.g.nodes:
            peso=0
            for c in self.g.neighbors(n):
                peso+=self.g[n][c]["weight"]
            lista.append(f"Nodo {n.id}: somma pesi archi adiacenti è {peso}")
        return lista
    def getBP(self):
        parziale=[]
        for x in self.g.nodes:
            parziale.append(x)
            visitabili=self.getVisitabili(x,parziale,0)
            self.ricorsione(parziale,visitabili)
            parziale.pop()
        return self.pesoMax

    def ricorsione(self, parziale, visitabili):
        peso=self.calcola(parziale)
        if peso>self.pesoMax:
            self.pesoMax=peso
            self.BP=copy.deepcopy(parziale)
        if len(visitabili)==0:
            return
        for node in visitabili:
            parziale.append(node)
            ultimoPeso=self.g[parziale[-2]][node]["weight"]
            newVis=self.getVisitabili(node,parziale,ultimoPeso)
            self.ricorsione(parziale,newVis)
            parziale.pop()




    def getLista(self):
        l=[]
        for i in range(0, len(self.BP)-1):
            x1=self.BP[i]
            x2=self.BP[i+1]
            l.append(f"{x1.id}--->{x2.id}, weight: {self.g[x1][x2]["weight"]},"
                     f" distance={distance((x1.Lat,x1.Lng),(x2.Lat,x2.Lng)).km}")
        return l

    def getVisitabili(self, x, parziale,ultimoPeso):
        lista=[]
        for i in self.g.neighbors(x):
            if i not in parziale and self.g[x][i]["weight"]>ultimoPeso:
                lista.append(i)
        return lista
        pass

    def calcola(self, parziale):
        tot=0
        for i in range(0,len(parziale)-1):
            tot+=distance((parziale[i].Lat,parziale[i].Lng),(parziale[i+1].Lat,parziale[i+1].Lng)).km
        return tot



