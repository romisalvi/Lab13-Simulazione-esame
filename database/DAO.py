from database.DB_connect import DBConnect
from model.State import State


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getYears():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select distinct YEAR(s.`datetime`) as y
from new_ufo_sightings.sighting s 
order by YEAR(s.`datetime`) desc
    """
        cursor.execute(query)
        for row in cursor:
            result.append(row["y"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getShapes():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select distinct s.Shape as y
    from new_ufo_sightings.sighting s 
    
        """
        cursor.execute(query)
        for row in cursor:
            result.append(row["y"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getStatiePeso(shape,anno):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT 
    s2.*, 
    COUNT(s.id) AS Sightings
FROM 
    new_ufo_sightings.state s2
LEFT JOIN 
    new_ufo_sightings.sighting s ON s2.id = s.state 
    AND YEAR(s.`datetime`) =%s 
    AND s.shape =%s
GROUP BY 
    s2.id;

                """
        cursor.execute(query,(anno,shape,))
        for row in cursor:
            result.append(State(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getConfini():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select N.*
from new_ufo_sightings.neighbor n 
where n.state1 < n.state2 
                """
        cursor.execute(query)
        for row in cursor:
            result.append((row["state1"],row["state2"]))
        cursor.close()
        conn.close()
        return result