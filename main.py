from inventory import Inventory
from item import Item
from cart import Cart

def main():
    inventory = Inventory("inventory.csv")
    cart = Cart()

    
    print("===Welcome to the Store===")
    
    inventory.display_items()


if __name__ == "__main__":
    main()  