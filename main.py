from src.binary_converter import BinaryConverter

def main() -> int:
    n: int = int(input('Enter a integer: '))
    b: BinaryConverter = BinaryConverter(n)
    print(b)

    return 0


if __name__ == '__main__':
    main()

