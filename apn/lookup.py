import jellyfish

from apn import APNS, ABBR_RE


def lookup(state=None, county=None):
    [x for x in APNS if x.state_field == state and x.county == county]
    if state is None:
        if ABBR_RE.match(state):
            state = state.upper()
            state_field = 'state_abbrev'
        else:
            state = jellyfish.metaphone(unicode(state, encoding='utf-8'))
            state_field = 'state_name_metaphone'
    elif state is not None:
        state_field = 'state'

    if county is None:
        county = jellyfish.metaphone(unicode(county, encoding='utf-8'))
        county_field = 'county_name_metaphone'

    elif county is not None:
        county_field = 'county'

    to_return = []
    for apn in APNS:
        if state == getattr(apn, state_field) and county == getattr(apn, county_field):
            to_return.append(apn)
    return to_return
