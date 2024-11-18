from abc import ABC, abstractmethod
from packaging import Packaging
from payment import Payable, PayType
from combine import Combinable

class DessertItem(Packaging):
  '''Parent Class, inherits name required to be of type string'''
  def __init__(self, name: str = "", tax_percent: float = 7.25):
    super().__init__()    
    self.name = name
    self.tax_percent = 7.25

  @abstractmethod
  def calculate_cost(self) -> float:
    pass

  def calculate_tax(self) -> float:
    return self.calculate_cost() * (self.tax_percent / 100)
  
  # Implement the Comparison Operators for cost
  def __gt__(self, other):
    return self.calculate_cost() > other.calculate_cost()
  
  def __ge__(self, other):
    return self.calculate_cost() >= other.calculate_cost()
  
  def __eq__(self, other):
    return self.calculate_cost() == other.calculate_cost()
  
  def __ne__(self, other):
    return self.calculate_cost() != other.calculate_cost()
  
  def __lt__(self, other):
    return self.calculate_cost() < other.calculate_cost()
  
  def __le__(self, other):
    return self.calculate_cost() <= other.calculate_cost()

class Candy(DessertItem):
  '''Child class of DessertItem'''
  def __init__(self, name : str ='', candy_weight: float = 0.0, price_per_pound: float = 0.0):
    super().__init__(name)
    self.candy_weight = candy_weight
    self.price_per_pound = price_per_pound
    self.packaging = "Bag"

  def calculate_cost(self):
    return self.price_per_pound * self.candy_weight
  
  #These are just meant to make building table possible.
  @property
  def quantity(self):
      return f"{self.candy_weight} lbs"
  
  #Again, just making these so I can access the prices for the table.
  @property
  def unit_price(self):
      return f"${self.price_per_pound}/lb"
  
  def __str__(self):
    cost = round(self.calculate_cost(), 2)
    tax = round(self.calculate_tax(), 2)
    return f'{self.candy_weight}lbs. @ ${self.price_per_pound}/lb, ${cost}, ${tax}, {self.packaging}'

  def can_combine(self, other:"Candy")->bool:
    return (
      isinstance(other, Candy) and
      self.name == other.name and
      self.price_per_pound == other.price_per_pound
    )
  
  def combine(self, other: "Candy") -> "Candy":
    if not self.can_combine(other):
      raise ValueError("Cannot combine different candies")
    self.candy_weight += other.candy_weight


class Cookie(DessertItem):
  '''Child class of DessertItem'''
  def __init__(self, name : str ='', cookie_quantity: int = 0, price_per_dozen: float = 0.0):
    super().__init__(name)
    self.cookie_quantity = cookie_quantity
    self.price_per_dozen = price_per_dozen
    self.packaging = "Box"

  def calculate_cost(self):
    return (self.price_per_dozen / 12) * self.cookie_quantity
  
  #These are just meant to make building table possible.
  @property
  def quantity(self):
      return f"{self.cookie_quantity} cookies"

  @property
  def unit_price(self):
      return f"${self.price_per_dozen}/dozen"
  
  def __str__(self):
    cost = round(self.calculate_cost(), 2)
    tax = round(self.calculate_tax(), 2)
    return f'{self.name}, {self.cookie_quantity} Cookies, ${self.price_per_dozen}/dozen, ${cost}, ${tax}, {self.packaging}'

  def can_combine(self, other:"Cookie")->bool:
    return (
      isinstance(other, Cookie) and
      self.name == other.name and
      self.price_per_dozen == other.price_per_dozen
    )
  
  def combine(self, other: "Cookie") -> "Cookie":
    if not self.can_combine(other):
      raise ValueError("Cannot combine different candies")
    self.cookie_quantity += other.cookie_quantity

class IceCream(DessertItem):
  '''Child class of DessertItem'''
  def __init__(self, name : str ='', scoop_count: int = 0, price_per_scoop: float = 0.0):
    super().__init__(name)
    self.scoop_count = scoop_count
    self.price_per_scoop = price_per_scoop
    self.packaging = "Bowl"

  def calculate_cost(self):
    return self.price_per_scoop * self.scoop_count
  
  #These are just meant to make building table possible.
  @property
  def quantity(self):
      return f"{self.scoop_count} scoops"

  @property
  def unit_price(self):
      return f"${self.price_per_scoop}/scoop"
  
  def __str__(self):
    cost = round(self.calculate_cost(), 2)
    tax = round(self.calculate_tax(), 2)
    return f'{self.name}, {self.scoop_count} Scoops, ${self.price_per_scoop}/scoop, ${cost}, ${tax}, {self.packaging}'

class Sundae(IceCream):
  '''Child class of IceCream, Grandchild class of DessertItem'''
  def __init__(self, name : str ='', scoop_count: int = 0, price_per_scoop: float = 0.0, topping_name: str ='', topping_price: float = 0.0):
    super().__init__(name)
    self.scoop_count = scoop_count
    self.price_per_scoop = price_per_scoop
    self.topping_name = topping_name
    self.topping_price = topping_price
    self.packaging = "Boat"

  def calculate_cost(self):
    return (self.scoop_count * self.price_per_scoop) + self.topping_price
  
  #These are just meant to make building table possible.
  @property
  def unit_price(self):
      return f"${self.price_per_scoop}/scoop"
  
  def __str__(self):
    cost = round(self.calculate_cost(), 2)
    tax = round(self.calculate_tax(), 2)
    return f'{self.name}, {self.scoop_count} Scoops, ${self.price_per_scoop}/scoop, ${cost}, ${tax}\n{self.topping_name}, ${self.topping_price}, {self.packaging}'


class Order(Payable):
  """Takes all the object of each order and uses them as a cart for calculation."""
  def __init__(self, pay_type: PayType = "CASH"):
    self._pay_type = pay_type
    self.order = []
    self._index = 0

  def add(self, item):
    if isinstance(item, Combinable): # We need to see if the item is combinable with the new item
      for working_item in self.order: # Go through the order and check for similarities to combine
        if isinstance(working_item, Combinable) and working_item.can_combine(item):
          working_item.combine(item)
          return # Return before adding new items
      self.order.append(item)
    else:
      self.order.append(item) # If the item isn't combinable, just add the order as a whole to the receipt.

    # Here we want to work on the iterations
    def __iter__(self):
      self._index = 0
      return self
    
    def __next__(self):
      if self._index < len(self.order):
        item = self.order[self._index]
        self._index += 1
        return item
      else:
        return StopIteration # Stop the iteration of the order.

  def __len__(self):
    return len(self.order)

  def order_cost(self):
    cost = 0.0
    for item in self.order:
      cost += item.calculate_cost()
    return cost

  def order_tax(self):
    tax = 0.0
    for item in self.order:
      tax += item.calculate_tax()
    return tax
  
  # Sorting Method
  def sort(self):
     self.order.sort(key=lambda item: item.calculate_cost())

  #Here we implement the Payable parent class methods and modify them
  def get_pay_type(self)->PayType:
     return self._pay_type
  
  def set_pay_type(self, payment_method: PayType)->None:
     self._pay_type = payment_method

  def __str__(self):
        payment_str = f"Paid with {self._pay_type}"
        items_str = "\n".join(str(item) for item in self.order)
        return f"{items_str}\n{payment_str}"