# TO DO 
# - Can create instance of Checkout class
# - Can add item price
# - Can calculate the current total
# - Can add multiple items and get correct total
# - Can add discount rules
# - Can apply discount rules to the total
# - Exception is thrown for item added without a price

# Checkout Kata Practice Session 28/5/2021

import pytest
from checkout import Checkout

@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.addItemPrice("a", 1)
    checkout.addItemPrice("b", 2)
    return checkout

def test_CanCalculateTotal(checkout):
    checkout.addItem("a")
    assert checkout.calculateTotal() == 1

def test_GetCorrectTotalWithMultipleItems(checkout):
    checkout.addItem("a")
    checkout.addItem("b")
    assert checkout.calculateTotal() == 3

def test_canAddDiscountRule(checkout):
    checkout.addDiscount("a", 3, 2)

# @pytest.mark.skip
def test_canApplyDiscountRule(checkout):
    checkout.addDiscount("a", 3, 2)
    checkout.addItem("a")
    checkout.addItem("a")
    checkout.addItem("a")
    assert checkout.calculateTotal() == 2

def test_ExceptionWithBadItem(checkout):
    with pytest.raises(Exception):
        checkout.addItem("c")

# def test_AssertTrue():
    # assert True

# import pytest
# from checkout import Checkout

# @pytest.fixture()
# def checkout():
#     checkout = Checkout()
#     checkout.addItemPrice("a", 1)
#     checkout.addItemPrice("b", 2)
    
#     return checkout

# def test_CanCalculateTotal(checkout):
#     checkout.addItem("a")
#     assert checkout.calculateTotal() == 1

# def test_GetCorrectTotalWithMultipleItems(checkout):
#     checkout.addItem("a")
#     checkout.addItem("b")
#     assert checkout.calculateTotal() == 3

# def test_canAddDiscountRule(checkout):
#     checkout.addDiscount("a", 3, 2)

# def test_canApplyDiscountRule(checkout):
#     checkout.addDiscount("a", 3, 2)

# # @pytest.mark.skip
# def test_canApplyDiscountRule(checkout):
#     checkout.addDiscount("a", 3, 2)
#     checkout.addItem("a")
#     checkout.addItem("a")
#     checkout.addItem("a")
#     assert checkout.calculateTotal() == 2

# def test_ExceptionWithBadItem(checkout):
#     with pytest.raises(Exception):
#         checkout.addItem("c")