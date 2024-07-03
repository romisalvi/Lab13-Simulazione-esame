from database.DB_connect import DBConnect
from model.State import State


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAnni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select  year(s.`datetime`) as y, count(s.id) as s
from new_ufo_sightings.sighting s
where s.country = 'us'
group by year(s.`datetime`)

        """

        cursor.execute(query)

        for row in cursor:
            result.append((row["y"], row["s"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getStati(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select s2.*
from new_ufo_sightings.sighting s
join new_ufo_sightings.state s2  on s2.id =s.state 
where s.country = 'us' and year(s.`datetime`)=%s
group by s2.id
        """

        cursor.execute(query,(anno,))

        for row in cursor:
            result.append(State(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAvvistamenti(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select s.state as st,s2.state as st2
from new_ufo_sightings.sighting s 
join new_ufo_sightings.sighting s2 on s2.state !=s.state
where year(s2.`datetime`)=%s and year(s.`datetime`)=%s and s2.`datetime` >s.`datetime`
group by s.state,s2.state"""

        cursor.execute(query, (anno,anno,))

        for row in cursor:
            result.append((row["st"], row["st2"]))


        cursor.close()
        conn.close()
        return result





