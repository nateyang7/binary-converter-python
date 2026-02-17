"""
Author: Nathan Yang
"""

class BinaryConverter:
    """
    Class representing a binary converter.

    Attributes:
        __n (int): Integer to convert. (DEFAULT: 0)
    """
    DIGITS: list = [str(digit) for digit in range(10)] + [chr(digit) for digit in range(65, 71)]
    BASE_DIGITS: dict = {n: digit for n, digit in enumerate(DIGITS)}

    def __init__(self, n_init: int = 0) -> None:
        """
        Initializes the binary converter.
        """
        self.__n = n_init
        self.__bits = [0]

    def get_integer(self) -> int:
        return self.__n

    def set_integer(self, new_integer: int) -> None:
        self.__n = new_integer

    def get_bits(self) -> list[int]:
        return self.__bits

    def set_bits(self, new_bits: list[int]) -> None:
        self.__bits = new_bits

    def convert_to_base(b: int) -> str:
        """
        Converts the current integer in a specific base.

        Args:
            b (int): Base to convert into.

        Returns
            str: Current integer convert to base b

        Examples:
            >>> b = BinaryConverter(15)
            >>> b.convert_to_base(16)
            'F'
        """
        n: int = self.get_integer()
        remainders: list[int] = []
        while n / base != 0:
            remainders.append(integer %  base)
            n //= base
        return ''.join(BASE_DIGITS[remainder] for remainder in remainders[::-1])



    def bin(self) -> str:
        """
        Converts an integer to binary depending on the number of bits.

        Returns:
            str: String of the integer converted to binary.

        Examples:
            >>> b = BinaryConverter()
            >>> b.set_integer(10)
            >>> b.bin()
            '1010'
        """
        n: int = self.get_integer()
        bits: list[int] = []
        while n / 2 != 0:
            bits.append(n % 2)
            n //= 2
        return ''.join(str(bit) for bit in bits[::-1])
        
    def oct(self) -> str:
        """
        Converts an integer to a octal notation.

        Returns:
            str: String of the integer converted to octal notation.

        Examples:
            >>> b = BinaryConverter()
            >>> b.set_integer(255)
            >>> b.oct()
            '377'
        """
        ...

    def hex(self) -> str:
        """
        Converts an integer to a hex number.

        Returns:
            str: String of the integer converted hexadecimal.

        Examples:
            >>> b = BinaryConverter()
            >>> b.set_integer(26)
            >>> b.hex()
            '1A'
        """
        ...

    def __repr__(self) -> str:
        return f"BIN: {self.bin()}"


print(BinaryConverter().BASE_DIGITS)
