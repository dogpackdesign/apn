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
            fuzzy_state = max(APNS, key=lambda x: fuzz.ratio(state, x.state)).state
            state_ratio = fuzz.ratio(state.lower(), fuzzy_state.lower())
            if state_ratio < 80:
                raise Exception('Invalid input state: ' + state + '. Fuzz Ratio: ' + str(state_ratio))
            state = fuzzy_state
            state_field = 'state'
        state_sub = filter(lambda x: state == getattr(x, state_field), APNS)
        if not state_sub:
            raise Exception('Invalid input state: ' + state)

    # county stuff
    county_sub = []
    if county is not None and state_sub:
        fuzzy_county = max(state_sub, key=lambda x: fuzz.ratio(county, x.county)).county
        county_ratio = fuzz.ratio(county.lower(), fuzzy_county.lower())
        if county_ratio < 80:
            raise Exception('Invalid input county: ' + county + '. Fuzz Ratio: ' + str(county_ratio))
        county = fuzzy_county
        county_field = 'county'
        county_sub = filter(lambda x: county == getattr(x, county_field), state_sub)
    elif county is not None and not state_sub:
        raise Exception('State is required when searching by county')

    if county_sub:
        apn_results = find_apn(apn_input=apn_input, apn_list=county_sub)
    elif not county_sub and state_sub:
        apn_results = find_apn(apn_input=apn_input, apn_list=state_sub)
    else:
        apn_results = find_apn(apn_input=apn_input, apn_list=APNS)

    return apn_results


def find_apn(apn_input, apn_list):
    try:
        apn_results = filter(lambda x: re.compile(x.apn_regex).match(apn_input), apn_list)
    except sre_constants as e:
        print 'ERROR: poorly formatted REGEX'
        pass
    if not apn_results:
        raise Exception('No formats for given APN')
    return apn_results
