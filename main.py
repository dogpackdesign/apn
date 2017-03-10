from apn import apn
from datetime import datetime


def main():
    start = datetime.now()
    lookup = apn.lookup('Washington', 'King')
    end = datetime.now()
    print lookup
    print end - start


if __name__ == '__main__':
    main()
