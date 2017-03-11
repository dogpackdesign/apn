import re
import sre_constants
from apn import APNS


def validate(apn_input, state=None, county=None):
    regex_add = []
    if state and county is not None:
        for apn in APNS:
            if state == getattr(apn, 'state_abbrev') and county == getattr(apn, 'county'):
                regex_add.append(re.compile(apn.apn_regex))

    elif county is None and state is not None:
        for apn in APNS:
            if state == getattr(apn, 'state_abbrev'):
                regex_add.append(re.compile(apn.apn_regex))

    elif state is None and county is None:
        for apn in APNS:
            try:
                regex_add.append(re.compile(apn.apn_regex))
            except sre_constants.error:
                print 'ERROR:', apn.state, apn.county, apn.apn_regex
                pass

    if any(regex.match(apn_input) for regex in regex_add):
        return True
    else:
        return False