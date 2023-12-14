from menu_item import Menu_Items

    
class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        cursor.execute("SELECT * FROM Menu_Items WHERE item_name = %s", (name,))
        result = cursor.fetchone()
        if result:
            return MenuItem(result[1], result[2])
        return None

    