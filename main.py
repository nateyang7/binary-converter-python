from src.binary_converter.binary_converter import *

def main() -> int:
    n: int = int(input("Enter a integer: "))
    b: BinaryConverter = BinaryConverter(n)
    print(b)
    return 0


if __name__ == "__main__":
    main()

