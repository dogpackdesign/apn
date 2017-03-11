from datetime import datetime

from apn import validate


def main():
    start = datetime.now()
    print validate.validate('123456-1234', state='WAshi', county='Kingl')
    end = datetime.now()
    print end - start


if __name__ == '__main__':
    main()
