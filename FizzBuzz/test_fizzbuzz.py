# TODO
# - Can I call FizzBuzz?
# - Get "1" when I pass in 1?
# - Get "2" when I pass in 2?
# - Get "Fizz" when I pass in 3?
# - Get "Buzz" when I pass in 5?
# - Get "Fizz" when I pass in 6 (a multiple of 3)?
# - Get "Buzz" when I pass in 10 (a multiple of 5)?
# - Get "FizzBuzz" when I pass in 15 (a multiple of 3 and 5)? 

import pytest

def fizzBuzz(value):
    if isMultiple(value, 3):
        if isMultiple(value, 5):
            return "FizzBuzz"  
        return "Fizz"
    if isMultiple(value, 5):
        return "Buzz"
    return str(value)

def isMultiple(value, mod):
    return(value % mod) == 0

def checkFizzBuzz(value, expectedRetVal):
    retVal = fizzBuzz(value)
    assert retVal == expectedRetVal

def test_returns1With1PassedIn():
    checkFizzBuzz(1, "1")

def test_returns2With2PassedIn():
    checkFizzBuzz(2, "2")

def test_returnsFizzWith3PassedIn():
    checkFizzBuzz(3, "Fizz")

def test_returnsBuzzWith5PassedIn():
    checkFizzBuzz(5, "Buzz")

def test_returnsFizzWith6PassedIn():
    checkFizzBuzz(6, "Fizz")

def test_returnsBuzzWith10PassedIn():
    checkFizzBuzz(10, "Buzz")

def test_returnsFizzBuzzWith15PassedIn():
    checkFizzBuzz(15, "FizzBuzz")