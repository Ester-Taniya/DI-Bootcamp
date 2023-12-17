from DB_conect import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()
    


class MenuManager:

    def __init__(self, city_name):
        self.city_name = city_name
    

    @classmethod
    def get_by_name(cls, city_name):
        cursor.execute("SELECT * FROM   WHERE en_name = %s", (city_name,))

        row = cursor.fetchall()
        if row:
            print(row[0][1], row[0][2])
        else:
            print("The city not found.")
        

        '''
        

    @classmethod
    def all_items(cls):
        cursor.execute("SELECT * FROM Menu_Items")

        rows = cursor.fetchall()
        for row in rows:
            print(list(row))
'''
           

                    







