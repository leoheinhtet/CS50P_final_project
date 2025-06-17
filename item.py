#item class with validation
class Item:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantiy = quantity
    #validating for name
    @property
    def name(self):
        return self.__name 
    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string.")
        self.__name = value.strip()
    #validating for price
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, value: float):
        if not isinstance(value, (int, float)) or value <0:
            raise ValueError("Price must be a non-negatice number")
        self.__price = float(value)

    #validating for quantity
    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self, value: int):
        if not isinstance(value, int) or value <0:
            raise ValueError("Quantity must be a non-negative integer.")

    
        
    
    