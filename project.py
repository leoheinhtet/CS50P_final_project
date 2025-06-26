from inventory import Inventory
from item import Item
from cart import Cart
from datetime import datetime
import csv

def generate_receipt_id(counter_file="receipt_counter.txt"):
    try:
        with open(counter_file, "r") as file:
            last_id = int(file.read().strip())
    except FileNotFoundError:
        last_id = 0

    new_id = last_id + 1

    with open(counter_file, "w") as file:
        file.write(str(new_id))

    return f"R{new_id:04d}"

def validate_add_to_cart(inventory, cart, item_id, quantity):
    item = inventory.get_item(item_id)
    if not item:
        return False, "Item not found."

    existing_in_cart = cart.items.get(item_id, [item, 0])[1]
    total_requested = existing_in_cart + quantity

    if inventory.is_in_stock(item_id, total_requested):
        return True, ""
    else:
        return False, f"Only {item.quantity} in stock. Cannot add {total_requested}."

def format_cart_summary(cart):
    lines = []
    for item, quantity in cart.get_items():
        total = item.price * quantity
        lines.append(f"{item.name} x{quantity} @ ${item.price:.2f} = ${total:.2f}")
    return "\n".join(lines) if lines else "Your cart is empty."

def main():
    inventory = Inventory("inventory.csv")
    cart = Cart()
    while True:
        try:
            print("===Welcome to the Store===")
            print("Menu:")
            print("1. View Items")
            print("2. Add Item to Cart")
            print("3. Remove Item from Cart")
            print("4. View Cart")
            print("5. Checkout")
            print("6. Exit")
            choice = int(input("Enter your choice (1-6): "))

            if choice == 1:
                inventory.display_items(cart)

            elif choice == 2:
                item_id = int(input("Enter the item ID to add to cart: "))
                amount = int(input("Enter the quantity to add: "))
                valid, message = validate_add_to_cart(inventory, cart, item_id, amount)
                if valid:
                    item = inventory.get_item(item_id)
                    cart.add_item(item, amount)
                    print(f"Added {amount} of {item.name} to cart.")
                else:
                    print(f"Error: {message}")

            elif choice == 3:
                print(cart)
                try:
                    reduce_item_id = int(input("Enter the item ID to remove from cart: "))
                    reduce_amount = int(input("Enter the quantity to remove: "))
                    cart.remove_item(reduce_item_id, reduce_amount)
                except ValueError as e:
                    print(f"Error: {e}")

            elif choice == 4:
                print(format_cart_summary(cart))

            elif choice == 5:
                if not cart.get_items():
                    print("Your cart is empty. Please add items before checking out.")
                else:
                    print("Checking out...")
                    receipt_id = generate_receipt_id()
                    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    try:
                        with open("sales.csv", mode="a", newline='', encoding='utf-8') as file:
                            writer = csv.writer(file)
                            if file.tell() == 0:
                                writer.writerow(["Receipt_ID", "Item_ID", "Item_Name", "Quantity", "Unit_Price", "Total_Price", "Timestamp"])
                            for item, quantity in cart.get_items():
                                total_price = item.price * quantity
                                inventory.update_stock(item.id, quantity)
                                writer.writerow([receipt_id, item.id, item.name, quantity, item.price, total_price, time_stamp])
                                print(f"Item: {item.name}, Quantity: {quantity}, Unit Price: ${item.price:.2f}, Total Price: ${total_price:.2f}")

                        print(f"Receipt ID: {receipt_id}")
                        print(f"Total Amount: ${cart.total_price():.2f}")
                        print("Thank you for your purchase!")
                        cart.clear()
                        inventory.save()
                    except Exception as e:
                        print(f"An error occurred during checkout: {e}")

            elif choice == 6:
                print("Exiting the store. Thank you!")
                break

        except ValueError as e:
            print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
