
from datetime import datetime

from apn import validate, lookup


def main():
    start = datetime.now()
    # print validate.validate('123456-1234')
    results = lookup.lookupken()
    print results
    end = datetime.now()
    print end - start


if __name__ == '__main__':
    main()
