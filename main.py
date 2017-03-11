
from apn import validate, lookup
import build


def main():
    # build.build()
    # apn.load_apns()
    start = datetime.now()
    validate_validate = validate.validate('14')
    print validate_validate
    print len(validate_validate)
    end = datetime.now()
    print end - start


if __name__ == '__main__':
    main()