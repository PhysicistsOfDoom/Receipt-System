import pytest
from dessert import Order, Candy

def test_card():
    order = Order("CARD")
    assert order._pay_type == "CARD"

def test_cash():
    order = Order("CASH")
    assert order._pay_type == "CASH"

def test_phone():
    order = Order("PHONE")
    assert order._pay_type == "PHONE"


# Testing the sort method in the order class
def test_sort():
    item1 = Candy("Candy Corn", 1.0, 2.0) # Medium
    item2 = Candy("Sucker", 1.0, 1.0) # Low
    item3 = Candy("Jaw Breaker", 1.0, 3.0) # High

    order = Order()

    order.add(item1)
    order.add(item2)
    order.add(item3)

    order.sort()

    assert order.order[0].calculate_cost() == 1.0
    assert order.order[1].calculate_cost() == 2.0
    assert order.order[2].calculate_cost() == 3.0

