#cart class to store items
class Cart:
    def __init__(self):

        self.items = []
    def add_item(self, item):
        """Add an item to the cart."""
        for i in self.items:
            if i["name"].lower()== item["name"].lower():
                i["quantity"] += item["quantity"]
                return
        self.items.append(item)

    def remove_item(self, item_name):
        """Remove an item from the cart by name."""
        self.items = [item for item in self.items if item["name"].lower() != item_name.lower()]

    def clear(self):
        """Clear the cart."""
        self.items = []

    def get_total(self):
        """Calculate the total price of items in the cart."""
        total = 0
        for item in self.items:
            total += item["price"] * item["quantity"]
        return total
    
    def is_empty(self):
        """Check if the cart is empty."""
        return len(self.items) == 0
    
    def __str__(self):
        """Return a string representation of the cart."""
        if self.is_empty():
            return "Your cart is empty"
        return "\n".join([f'{item["name"]}: {item["quantity"]} x ${item["price"]:.2f} =  ${item["quantity"] * item["price"]:.2f}' for item in self.items])
    
