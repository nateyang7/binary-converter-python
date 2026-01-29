import pytest
from binary_converter.binary_converter import BinaryConverter

@pytest.fixture
def binary_converter():
    return BinaryConverter()

def test_set_integer(binary_converter: BinaryConverter):
    binary_converter.set_integer(10)
    assert binary_converter.get_integer() == 10

def test_natural_integer_to_binary(binary_converter: BinaryConverter):
    binary_converter.set_integer(10)
    assert binary_converter.nat_bin() == [1, 0, 1, 0]

"""
def test_integer_to_binary(binary_converter):
    binary_converter.set_integer(-10)
    ...
"""

