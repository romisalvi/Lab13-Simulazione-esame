from database.DB_connect import DBConnect
from model.state import State


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
    def getShapesxYear( year):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select distinct s.shape as sh
            from new_ufo_sightings.sighting s 
            where year( s.`datetime` )=%s
                """
        cursor.execute(query,(year,))
        for row in cursor:
            result.append(row["sh"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getStatiePeso( ):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT 
        s.*
        from
        new_ufo_sightings.state s
        

                    """
        cursor.execute(query)
        for row in cursor:
            result.append(State(**row))
        cursor.close()
        conn.close()
        return result

