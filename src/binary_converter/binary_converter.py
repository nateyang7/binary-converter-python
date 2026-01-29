"""
Author: Nathan Yang

TO-DO:
    - [] Can convert integers with two's complement
"""

class BinaryConverter:
    """
    Class representing a binary converter.

    Attributes:
        __n (int): Integer to convert. (DEFAULT: 0)
    """

    def __init__(self) -> None:
        """
        Initializes the binary converter.
        """
        self.__n = 0
        self.__bits = [0]

    def get_integer(self) -> int:
        return self.__n

    def set_integer(self, new_integer: int) -> None:
        self.__n = new_integer

    def get_bits(self) -> list[int]:
        return self.__bits

    def set_bits(self, new_bits: list[int]) -> None:
        self.__bits = new_bits

    def nat_bin(self) -> list[int]:
        """
        Converts a natural integer to binary.

        Returns:
            str: String of the natural integer converted to binary

        Examples:
            >>> b = BinaryConverter()
            >>> b.set_integer(10)
            >>> b.nat_bin()
            [1, 0, 1, 0]
        """
        bits: str = []
        n: int = self.get_integer()
        while n / 2 != 0:
            bits.append(n % 2)
            n //= 2
        return bits[::-1]

    def reverse_bits(self) -> list[int]:
        """
        Reverse bits from a binary number.

        Returns:
            None.
        """
        for bit in self.__bits():
            bit = 0 if bit == 1 else 1

    def add(self, bits: list[int]) -> None:
        """
        Add bits to the current binary number.

        Args:
            bits (list[int]): List of bits of another number.

        Returns:
            None.
        """
        ...

    def bin(self, bits: int = 8) -> str:
        """
        Converts an integer to binary depending on the number of bits.

        Returns:
            str: String of the integer converted to binary.

        Examples:
            >>> b = BinaryConverter()
            >>> b.set_integer(-10)
            >>> b.bin()
            [1, 1, 1, 1, 0, 1, 1, 0]
        """
        if self.get_integer() >= 0:
            return self.nat_bin()
        bits_list: list[int] = self.nat_bin()
        while len(bits_list) != bits:  # Fill bits to get the size required
            bits_list.insert(0)
        print(bits_list)
        self.set_bits(bits_list)
        self.reverse_bits()




        
    def oct(self) -> str:
        """
        Converts an integer to a octal notation.

        Returns:
            str: String of the integer converted to octal notation.

        Examples:
            >>>
        """
        ...

    def hex(self) -> str:
        """
        Converts an integer to a hex number.

        Returns:
            str: String of the integer converted hexadecimal.

        Examples:
            >>>
        """
        ...

    def __repr__(self) -> str:
        ...

