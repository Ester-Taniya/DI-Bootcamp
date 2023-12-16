from DB_conect import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

class AlertItem:
    def __init__(self, id, city, time):
        self.id = id
        self.City = city
        self.Time = time

    

    def save(self):
        # Insert data into the "alerts" table
        cursor.execute(
            "INSERT INTO alerts (id, city, time) VALUES (%s, %s, %s)",
            (self.id, self.City, self.Time),
        )
        conn.commit()
