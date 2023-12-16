from DB_conect import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()



class Alert_item:
    def __init__(self, id, city, time):
        self.id = id
        self.city = city
        self.time=time
        

    def save(self):

        cursor.execute(
            "INSERT INTO alerts (id, city,time ) VALUES (%s, %s, %s)",
            (self.id, self.city, self.time),)
        conn.commit()
    cursor.close()
    conn.close()       






