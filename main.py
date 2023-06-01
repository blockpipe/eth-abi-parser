
from readable_abi import HumanReadableParser


def main():
    parser = HumanReadableParser(
        'event TestEvent(uint indexed id, (string, uint16, (uint8, uint8)) value)')
    print(parser.take_event())


if __name__ == '__main__':
    main()
