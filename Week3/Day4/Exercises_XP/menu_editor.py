from menu_manager import MenuManager
from menu_item import MenuItem

def show_user_menu():
    print("Menu Editor:")
    print("V - View an Item")
    print("A - Add an Item")
    print("D - Delete an Item")
    print("U - Update an Item")
    print("S - Show the Menu")
    print("X - Exit")



def add_item_to_menu():
    name = input("Enter item name: ")
    price = int(input("Enter item price: "))
    item = MenuItem(name, price)
    item.save()
    print()
    print("Item added successfully.")
    print()



def remove_item_from_menu():
    name = input("Enter item name: ")
    item = MenuItem(name,0)
    item.delete()
    print()
    print("Item deleted successfully.")
    print()


def update_item_from_menu():
    name = input("Enter item name to update: ")
    price = int(input("Enter new item price: "))
    new_name = input("Enter new item name: ")
    item = MenuItem(name, 0)  # Price doesn't matter for update
    item.update(new_name, price)
    print()
    print("Item updated successfully.")
    print()




def show_restaurant_menu():
    items = MenuManager.all_items()
    print("Restaurant Menu:")
    for item in items:
        print(f"{item.name} - ${item.price}")
        



while True:
    show_user_menu()
    choice = input("Enter your choice: ").upper()

    if choice == "V":
        name = input("Enter item name to view: ")
        item = MenuManager.get_by_name(name)
        if item is not None:
            print(f"{item.item_name} - ${item.item_price}")
        else:
            print("Item not found.")

    elif choice == "A":
        add_item_to_menu()

    elif choice == "D":
        remove_item_from_menu()

    elif choice == "U":
        update_item_from_menu()

    elif choice == "S":
        show_restaurant_menu()

    elif choice == "X":
        show_restaurant_menu()
    
        break

    else:
        print("Invalid choice. Please try again.")


#raise ValueError("Error.")