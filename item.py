#item class with validation
class Item:
    def __init__(self, id: int, name: str, price: float, quantity: int, category: str = None):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
    #validating for id
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("ID must be a non-negative integer.")
        self.__id = value
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
            raise ValueError("Price must be a non-negative number")
        self.__price = float(value)

    #validating for quantity
    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, value: int):
        if not isinstance(value, int) or value <0:
            raise ValueError("Quantity must be a non-negative integer.")
        self.__quantity = value

    #validating for category
    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self, value: str):
        if value is not None and not isinstance(value, str):
            raise ValueError("Category must be a string or None.")
        self.__category = value.strip() if value else None
    
     
    
    