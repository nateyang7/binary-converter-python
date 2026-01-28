"""
Author: Nathan Yang

TO-DO:
    - [] Can convert integers with two's complement
"""

class BinaryConverter:
    """
    Class representing a binary converter.

    Attributes:
        n (int): Integer to convert. (DEFAULT: 0)
    """

    def __init__(self) -> None:
        """
        Initializes the binary converter.
        """
        self.n = 0

    def get_integer(self) -> int:
        return self.n

    def set_integer(self, new_integer: int) -> None:
        self.n = new_integer

    def nat_bin(self) -> str:
        """
        Converts a natural integer to binary.

        Returns:
            str: String of the natural integer converted to binary
        """
        bits: str = ''
        n: int = self.get_integer()
        while n / 2 != 0:
            bits += str(n % 2)
            n //= 2
        return bits[::-1]

    def bin(self) -> str:
        """
        Converts an integer to binary.

        Returns:
            str: String of the integer converted to binary.

        Examples:
            >>>
        """
        
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

