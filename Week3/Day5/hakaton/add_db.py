from DB_conect import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

class AlertItem:
    def __init__(self, ID, City, Time):
        self.ID = ID
        self.City = City
        self.Time = Time

    def save(self):
        # Insert data into the "alerts" table
        cursor.execute(
            "INSERT INTO alerts (ID, City, \"Time\") VALUES (%s, %s, %s)",
            (self.ID, self.City, self.Time),
        )
        conn.commit()

    def print_all_rows(self):
        # Select and print all rows from the "alerts" table
        cursor.execute("SELECT * FROM alerts")
        rows = cursor.fetchall()
        for row in rows:
            print(list(row))

# Create an instance of AlertItem
item = AlertItem(122, 'dfgh', '2023-12-16 22:14:00')

# Save the item to the "alerts" table
item.save()

# Print all rows from the "alerts" table
item.print_all_rows()

# Close the cursor and connection
cursor.close()
conn.close()
