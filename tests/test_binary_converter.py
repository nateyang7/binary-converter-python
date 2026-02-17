import pytest
from binary_converter.binary_converter import BinaryConverter

@pytest.fixture
def binary_converter():
    return BinaryConverter()

def test_set_integer(binary_converter: BinaryConverter):
    binary_converter.set_integer(10)
    assert binary_converter.get_integer() == 10

def test_convert_to_base(binary_converter: BinaryConverter):
    binary_converter.set_integer(15)
    assert binary_converter.convert_to_base(2) == '1111'
    assert binary_converter.convert_to_base(8) == '17'
    assert binary_converter.convert_to_base(16) == 'F'

def test_bin(binary_converter):
    binary_converter.set_integer(10)
    assert binary_converter.bin() == '1010'

def test_oct(binary_converter: BinaryConverter):
    binary_converter.set_integer(255)
    assert binary_converter.oct() == '377'

def test_hex(binary_converter: BinaryConverter):
    binary_converter.set_integer(26)
    assert binary_converter.hex() == '1A'
