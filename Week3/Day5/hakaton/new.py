from datetime import datetime
from DB_conect import get_db_connection

class AlertItem:
    def __init__(self, ID, City, Time):
        self.ID = ID
        self.City = City
        self.Time = Time

    def save(self):
        # Get a database connection
        conn = get_db_connection()

        # Use a context manager for handling the database connection
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO alerts (id, city, time) VALUES (%s, %s, %s)",
                (self.ID, self.City, self.Time),
            )
            conn.commit()

        # Close the connection
        conn.close()
        

# Example usage
item = AlertItem(223456, 'אילון', "2023-12-16 13:17:00")
item.save()


