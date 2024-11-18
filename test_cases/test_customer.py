import pytest
from dessertshop import Customer

def test_initialization():
    customer = Customer("Corbin")
    assert isinstance(customer.customer_name, str)
    assert customer.customer_name == "Corbin"
    assert customer.order_history == []
    assert Customer.id == 1
    
