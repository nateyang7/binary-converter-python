import pytest
from src.calculator import Calculator

@pytest.fixture
def test_calculator():
    return Calculator(2, 3)


def test_add(test_calculator):
    assert test_calculator.add() == 5


def test_subtract(test_calculator):
    assert test_calculator.subtract() == -1

def test_multiply(test_calculator):
    assert test_calculator.multiply() == 6

