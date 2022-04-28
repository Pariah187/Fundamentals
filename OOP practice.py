# %%
import csv

class Item:
    discount_rate = 0.8 # Price after 20% discount
    all = []
    def __init__(self, name:str, price:float, quantity=0):

        # Run validations to the received arguments(parameters)
        assert price >=0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >=0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Update all list on instantiate
        Item.all.append(self)

    @property
    # Property Decorator = Read-Only
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

    @property
    def price(self):
        return self.__price

    def calculate_total_price(self):
        return self.__price * self.quantity

    def apply_discount(self):
        self.__price = self.__price * self.discount_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price + increment_value


    # Method for calculating total price    


    @classmethod
    # Class methods are usually used to manipulate data structures when instantiating objects.
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = str(item.get('name')),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )

    @staticmethod
    # Choose static for methods that have a relationship with the class, but do not need to be unique per instance.
    def is_integer(num):
        # We will count out the floats that are actually integers.
        # i.e: 5.0. 10.0
        if isinstance(num, float):
            # floats that are actually integers
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    #print(Item.all)
    def __repr__(self):
        return f"{self.__class__.__name__},'{self.name}', '{self.__price}', '{self.quantity}')"

class Phone(Item):
    def __init__(self, name:str, price:float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )
        # Run validation for new attribute
        assert broken_phones >=0, f"Quantity of {broken_phones} is not greater than or equal to zero!"

        # Assign to self object
        self.broken_phones = broken_phones
    
class Laptop(Item):
    def __init__(self, name:str, price:float, quantity=0, broken_phones=0):
        super().__init__(
            name, price, quantity
        )

class Keyboard(Item):
    def __init__(self, name:str, price:float, quantity=0, broken_phones=0):
        super().__init__(
            name, price, quantity
        )
class Mouse(Item):
    def __init__(self, name:str, price:float, quantity=0, broken_phones=0):
        super().__init__(
            name, price, quantity
        )
class Cable(Item):
    def __init__(self, name:str, price:float, quantity=0, broken_phones=0):
        super().__init__(
            name, price, quantity
        )



Item.instantiate_from_csv()
print(Laptop.all)
print(Phone)




# %%