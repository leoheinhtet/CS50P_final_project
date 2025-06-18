#cart class to store items
class Cart:
    def __init__(self):
        self.items = {} # key: item.id, value: (Item, quantity)

    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item.id][1] += quantity
        self.items[item.id] = (item, quantity)

    def remove_item(self, item):
        if item.id in self.items:
            del self.items[item.id]
        else:
            raise ValueError("Item not found in cart")
        
    def get_items(self):
        return self.items.values()
    
    def clear(self):
        self.items.clear()

    def total_price(self):
        total = 0
        for item, quantity in self.items.values():
            total += item.price * quantity
        return total
    
    def __str__(self):
        if len(self.items) == 0:
            return "Your cart is empty."
        items_str = []
        for item, quantity in self.items.values():
            items_str.append(f"{item.name}:  {quantity} @ ${item.price:.2f}each")

        return "\n".join(items_str)
    