#inventory class for csv management
from item import Item
import csv

class Inventory:
    def __init__ (self, filename='inventory.csv'):
        """Initialize the inventory with a CSV file."""
        self.filename = filename
        self.stock = {}
        self.stock = self.load_inventory()

    def load_inventory(self):
        """Load items from the CSV file into the inventory."""
        
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    item = Item(
                        id = row['id'],
                        name = row['name'],
                        price = row['price'],
                        quantity = row['quantity'],
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
        if self.is_in_stock(item_id, amount):

            item = self.get_item(item_id)
            item.quantity -= amount
        else:
            raise  ValueError("Not enough stock available for this item.")
        
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

    def __str__(self):
        return "\n".join(str(item) for item in self.stock.values())

    
    
        

                    