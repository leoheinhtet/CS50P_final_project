#inventory class for csv management
from item import Item
import csv

class Inventory:
    def __init__ (self, filename='inventory.csv'):
        """Initialize the inventory with a CSV file."""
        self.filename = filename
        self.stock = self.load_inventory()

    def load_inventory(self):
        """Load items from the CSV file into the inventory."""
        stock = {}
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name = row['name'].strip()
                    price = float(row["price"])
                    quantity = int(row["quantity"])
                    stock[name.lower()] = Item(name, price, quantity)
        except FileNotFoundError:
            print(f"Error: The file {self.filename} does not exist.")

        return stock
    
    
        

                    