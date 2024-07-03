from database.DAO import DAO


class Model:
    def __init__(self):
        pass
    def getYears(self):
        return DAO.getYears()
    def getShapesxYear(self,year):
        return DAO.getShapesxYear(year)
    def getStates(self):
        return DAO.getStatiePeso()