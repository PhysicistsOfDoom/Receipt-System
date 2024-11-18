import pytest
from dessert import Candy

def test_candy():
  candy = Candy("Taffy", 1.0, 2.0)
  assert candy.name == 'Taffy'
  assert candy.candy_weight == 1.0
  assert candy.price_per_pound == 2.0
  assert candy.calculate_cost() == 2.0