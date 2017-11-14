import time

import apn
import cProfile


def main():
    print(apn.lookup("WA", "KING"))
    # apn.lookup('WA', 'King')
    cProfile.run('apn.lookup("WA", "King")')


if __name__ == '__main__':
    main()
