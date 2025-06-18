from inventory import Inventory
from item import Item
from cart import Cart

def main():
    inventory = Inventory("inventory.csv")
    cart = Cart()
    while True:
        try:
            print("===Welcome to the Store===")
            print("Menu:")
            print("1. View Items")
            print("2. Add Item to Cart")
            print("3. View Cart")
            print("4. Checkout")
            print("5. Exit")
            choice = int(input("Enter your choice (1-5): "))

            if choice == 1:
                inventory.display_items()

            elif choice == 2:
                item_id = int(input("Enter the item ID to add to cart: "))
                amount = int(input("Enter the quantity to add: "))
                item = inventory.get_item(item_id)
                if item:
                    if inventory.is_in_stock(item_id, amount):
                        cart.add_item(item, amount)
                        inventory.update_stock(item_id, amount)
                        print(f"Added {amount} of {item.name} to cart.")
                    else:
                        print("Not enough stock available for this item.")

            elif choice == 3:
                print(cart)

            elif choice == 4:
                if not cart.get_items():
                    print("Your cart is empty. Please add items before checking out.")
                else:
                    print("Checking out...")
                    try:
                        for item, quantity in cart.get_items():
                            inventory.update_stock(item.id, quantity)
                        print(f"Total price: ${cart.total_price():.2f}")
                        cart.clear()
                        print("Thank you for your purchase!")
                    except ValueError as e:
                        print(f"Error during checkout: {e}")
            
            elif choice == 5:
                print("Exiting the store. Thank you!")
                break

        except ValueError as e:
            print(f"Invalid input: {e}")



    
    


if __name__ == "__main__":
    main()  