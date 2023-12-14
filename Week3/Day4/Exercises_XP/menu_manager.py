from DB_conect import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()
    


class MenuManager:

    def __init__(self, item_name):
        self.item_name = item_name
    
    @classmethod
    def get_by_name(cls, item_name):
        cursor.execute("SELECT * FROM Menu_Items WHERE item_name = %s", (item_name,))

        row = cursor.fetchall()
        if row:
            print(row[0][1], row[0][2])
        else:
            print("Item not found.")

    @classmethod
    def all_items(cls):
        cursor.execute("SELECT * FROM Menu_Items")

        rows = cursor.fetchall()
        for row in rows:
            print(list(row))
        

item=MenuManager(1)
item.get_by_name('test3')

   

