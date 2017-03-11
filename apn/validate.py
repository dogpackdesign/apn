import re
import sre_constants

from fuzzywuzzy import fuzz

from apn import APNS, ABBR_RE


def validate(apn_input, state=None, county=None):
    # state stuff
    state_sub = []
    if state is not None:
        if ABBR_RE.match(state):
            state = state.upper()
            state_field = 'state_abbrev'
        else:
            state = max(APNS, key=lambda x: fuzz.ratio(state, x.state)).state
            state_field = 'state'
        state_sub = filter(lambda x: state == getattr(x, state_field), APNS)

    # county stuff
    county_sub = []
    if county is not None and state_sub:
        county = max(state_sub, key=lambda x: fuzz.ratio(county, x.county)).county
        county_field = 'county'
        county_sub = filter(lambda x: county == getattr(x, county_field), state_sub)

    apn_results = []
    if county_sub:
        try:
            apn_results = filter(lambda x: re.compile(x.apn_regex).match(apn_input), county_sub)
        except sre_constants as e:
            print 'ERROR: poorly formatted REGEX'
            pass
    return apn_results
