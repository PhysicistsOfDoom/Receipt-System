import pytest
from dessert import IceCream

def test_icecream():
  icecream = IceCream("Taffy", 1.3, 3.50)
  assert icecream.name == 'Taffy'
  assert icecream.scoop_count == 1.3
  assert icecream.price_per_scoop == 3.50
  assert icecream.calculate_cost() == 1.3 * 3.50