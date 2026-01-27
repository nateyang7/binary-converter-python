"""
=== Module : Binary ===
Author: Nathan Yang
"""

def get_integer_binary(n: int) -> list[int]:
    """
    Returns a list of bits from  a natural integer converted to binary.

    Args:
        n (int): Natural number to convert to binary.

    Returns:
        list[int]: List of bits representing 'n' in binary.

    Examples:
        >>> get_integer_binary(10)
        [1, 0, 1, 0]
    """
    bits: list[int] = []
    n_cp: int = n
    while n_cp / 2 != 0:
        bits.append(n_cp % 2)
        n_cp //= 2
    return bits[::-1]


if __name__ == "__main__":
    assert get_integer_binary(5) == [1, 0, 1]  # OK


    print("All tests passed!")

