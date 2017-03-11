from datetime import datetime

from apn import apn


def main():
    start = datetime.now()
    lookup = apn.lookup('Washington', 'King')
    print lookup
    # print apn.validate('123456-1234')
    end = datetime.now()
    print end - start


if __name__ == '__main__':
    main()
