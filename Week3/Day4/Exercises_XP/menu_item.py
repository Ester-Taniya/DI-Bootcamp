from DB_conection import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

class MenuItem:
    def __init__(self, item_name, item_price=0):
        self.item_name = item_name
        self.item_price = item_price
        

    def save(self):
        cursor.execute(
            "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)",(self.name, self.price),)

        insert_qury='INSERT INTO public_items (item_name, item_price) VALUES (%s, %s)'
        data_to_insert = (self.name, self.price)
        cursor.execute.execute(insert_qury,data_to_insert)
        conn.commit()

    def delete(self):


        cursor.execute("DELETE FROM Menu_Items WHERE item_name = %s", (self.name,))
        conn.commit()

    def update(self, new_name, new_price):
        cursor.execute(
            "UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s",
            (new_name, new_price, self.name))
        conn.commit()
        
