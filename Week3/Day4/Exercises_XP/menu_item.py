from DB_conect import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()



class MenuItem:
    def __init__(self, item_name, item_price=0):
        self.item_name = item_name
        self.item_price = item_price
        

    def save(self):

        cursor.execute(
            "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)",
            (self.item_name, self.item_price),)
        conn.commit()
        

    def delete(self):

        cursor.execute("DELETE FROM Menu_Items WHERE item_name = %s", (self.item_name,))
        conn.commit()
       


    def update(self, new_name, new_price):
        cursor.execute(
            "UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s",
            (new_name, new_price, self.item_name))
        conn.commit()
        


#item = MenuItem('burger', 35)
#test= MenuItem('test2',0)
#test.delete()
#tem.save()

#item.update('new_burger', 40)