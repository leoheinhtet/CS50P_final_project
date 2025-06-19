#inventory class for csv management
from item import Item
import csv

class Inventory:
    def __init__ (self, filename='inventory.csv'):
        """Initialize the inventory with a CSV file."""
        self.filename = filename
        self.stock = {}
        self.load_inventory()

    def load_inventory(self):
        """Load items from the CSV file into the inventory."""
        
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    item = Item(
                        id = int(row['id']),
                        name = row['name'],
                        price = float(row['price']),
                        quantity = int(row['quantity']),
                        category = row['category'])
                    self.stock[item.id] = item
                    
        except FileNotFoundError:
            print(f"Error: The file {self.filename} does not exist.")

    def get_item(self, item_id):
        """Retrieve an item by its ID."""
        return self.stock.get(item_id, None)
    
    def is_in_stock(self, item_id, amount):
        """Check if an item is in stock."""
        item = self.get_item(item_id)
        if item and item.quantity >= amount:
            return True
        return False
    
    def update_stock(self, item_id, amount):
        """Update the stock of an item by its ID."""
        

        item = self.get_item(item_id)
        item.quantity -= amount
        
        
    def save(self):
        with open(self.filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'name', 'price', 'quantity', 'category'])
            writer.writeheader()
            for item in self.stock.values():
                writer.writerow({
                    'id': item.id,
                    'name': item.name,
                    'price': item.price,
                    'quantity': item.quantity,
                    'category': item.category
                })

    def display_items(self):
        if not self.stock:
            print("No items in inventory.")
            return

        print(f"{'ID':<4} {'Name':<20} {'Price($)':<10} {'Qty':<6} {'Category'}")
        print("-" * 60)
        for item in self.stock.values():
            print(f"{item.id:<4} {item.name:<20} {item.price:<10.2f} {item.quantity:<6} {item.category}")




