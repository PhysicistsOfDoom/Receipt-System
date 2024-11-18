import pytest
from dessert import Sundae

def test_sundae():
  sundae = Sundae("Taffy", 1.32, 2.55, "sprinkles", 1.40)
  assert sundae.name == 'Taffy'
  assert sundae.scoop_count == 1.32
  assert sundae.price_per_scoop == 2.55
  assert sundae.topping_name == "sprinkles"
  assert sundae.topping_price == 1.40
  assert sundae.calculate_cost() == (1.32 * 2.55) + 1.40