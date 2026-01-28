import pytest
from binary_converter import BinaryConverter

@pytest.fixture
def binary_converter():
    return BinaryConverter()

def test_set_integer(binary_converter):
    binary_converter.set_integer(10)
    assert binary_converter.get_integer() == 10

def test_convert_to_binary(binary_converter):
    binary_converter.set_integer(10)
    assert binary_converter.bin() == "1010"

