import pytest
from binary_converter.binary_converter import BinaryConverter

@pytest.fixture
def binary_converter():
    return BinaryConverter()

def test_set_integer(binary_converter: BinaryConverter):
    binary_converter.set_integer(10)
    assert binary_converter.get_integer() == 10

"""
def test_natural_integer_to_binary(binary_converter: BinaryConverter):
    binary_converter.set_integer(10)
    assert binary_converter.nat_bin() == [1, 0, 1, 0]
"""

def test_bin(binary_converter):
    binary_converter.set_integer(10)
    assert binary_converter.bin() == '1010'

"""
def test_oct(binary_converter: BinaryConverter):
    binary_converter.set_integer(255)
    assert binary_converter.oct() == '377'
"""

"""
def test_hex(binary_converter: BinaryConverter):
    binary_converter.set_integer()
    assert binary_converter.hex() == '1A'
"""
