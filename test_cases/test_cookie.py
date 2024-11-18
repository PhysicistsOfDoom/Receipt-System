import pytest
from dessert import Cookie

def test_cookie():
  cookie = Cookie("Snickerdoodle", 1.50, 2.99)
  assert cookie.name == 'Snickerdoodle'
  assert cookie.cookie_quantity == 1.50
  assert cookie.price_per_dozen == 2.99
  assert cookie.calculate_cost() == (1.50 / 12) * 2.99