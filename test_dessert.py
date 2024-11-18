import pytest
from dessert import DessertItem, Candy, Cookie, IceCream, Sundae

# Testing the class attributes & methods 
def test_dessert():
  dessert = DessertItem("dessert")
  assert dessert.name == 'dessert'
  assert dessert.tax_percent == 7.25
  
def test_icecream():
  icecream = IceCream("Taffy", 1.3, 3.50)
  assert icecream.name == 'Taffy'
  assert icecream.scoop_count == 1.3
  assert icecream.price_per_scoop == 3.50
  assert icecream.calculate_cost() == 1.3 * 3.50

def test_candy():
  candy = Candy("Taffy", 1.0, 2.0)
  assert candy.name == 'Taffy'
  assert candy.candy_weight == 1.0
  assert candy.price_per_pound == 2.0
  assert candy.calculate_cost() == 2.0

def test_sundae():
  sundae = Sundae("Taffy", 1.32, 2.55, "sprinkles", 1.40)
  assert sundae.name == 'Taffy'
  assert sundae.scoop_count == 1.32
  assert sundae.price_per_scoop == 2.55
  assert sundae.topping_name == "sprinkles"
  assert sundae.topping_price == 1.40
  assert sundae.calculate_cost() == (1.32 * 2.55) + 1.40

def test_cookie():
  cookie = Cookie("Snickerdoodle", 1.50, 2.99)
  assert cookie.name == 'Snickerdoodle'
  assert cookie.cookie_quantity == 1.50
  assert cookie.price_per_dozen == 2.99
  assert cookie.calculate_cost() == (1.50 / 12) * 2.99

# Testing operaters for instances
def test_operations():
  item1 = Candy("Candy Corbin", 1.0, 2.0)
  item2 = Candy ("Sucker", 1.0, 3.0)

  assert (item1 < item2) == True
  assert (item1 <= item2) == True
  assert (item1 >= item2) == False
  assert (item1 > item2) == False
  assert (item1 == item2) == False
  assert (item1 != item2) == True


# Here we test the combine.py usage to help us get the proper combinations.
def can_combine_true():
    cookie1 = Cookie("Chocolate Chip", 12, 5.0)
    cookie2 = Cookie("Chocolate Chip", 6, 5.0)
    assert cookie1.can_combine(cookie2) == True

def can_combine_false():
    cookie = Cookie("Chocolate Chip", 12, 5.0)
    not_cookie = None
    assert cookie.can_combine(not_cookie) == False

def combine_cookies():
    cookie1 = Cookie("Chocolate Chip", 12, 5.0)
    cookie2 = Cookie("Chocolate Chip", 6, 5.0)
    cookie1.combine(cookie2)
    assert cookie1.quantity == 18  # Quantity should be combined

def combine_not_cookie():
    cookie = Cookie("Chocolate Chip", 12, 5.0)
    not_cookie = None
    with pytest.raises(ValueError):
        cookie.combine(not_cookie)