from DB_conect import get_db_connection

class City:
    # Connect to the database
    conn = get_db_connection()

    def __init__(self, en_name):
        self.en_name = en_name

    def show(self):
        # Use a context manager for handling the database connection
        with self.conn.cursor() as cursor:
            cursor.execute(
                "SELECT city_id FROM city WHERE en_name = %s", (self.en_name,))

            row = cursor.fetchall()
            if row:
                return(row[0][0])
            else:
                return None #("Item not found")

        self.conn.commit()

# Create an instance of City
city1 = City('Tel Aviv')

# Call the show method on the instance
city1.show()

# Close the database connection outside the class when done
city1.conn.close()



                    







