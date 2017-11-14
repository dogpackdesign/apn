import pickle
import re

from fuzzywuzzy import process
from pkg_resources import resource_stream

ABBR_RE = re.compile(r'^[a-zA-Z]{2}$')
APNS = []
STATES = []
STATE_ABBREVS = []


class Apn(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __repr__(self):
        return "<APN:%s>" % self.state

    def __str__(self):
        return self.state

    @property
    def serialize(self):
        return {
            'apn_format': self.apn_format,
            'apn_regex': self.apn_regex,
            'county': self.county,
            'state': self.state
        }


def __load_apns():
    with resource_stream(__name__, 'data/apn.pkl') as apnpkl:
        for a in pickle.load(apnpkl):
            apn = Apn(**a)
            APNS.append(apn)


def __load_states():
    with resource_stream(__name__, 'data/state.pkl') as statepkl:
        for s in pickle.load(statepkl):
            STATES.append(s)

    with resource_stream(__name__, 'data/abbrev.pkl') as abbrevpkl:
        for ab in pickle.load(abbrevpkl):
            STATE_ABBREVS.append(ab)


def __load_data():
    __load_apns()
    __load_states()


def _find_by_state_county(state, county):
    by_state = _find_by_state(state)
    if county is not None:
        return [x for x in by_state if x['county'] == county]
    else:
        return by_state


def _find_by_state(state):
    if ABBR_RE.match(state):
        return [x.serialize for x in APNS if x.state_abbrev == state]
    else:
        return [x.serialize for x in APNS if x.state == state]


def _lookup_state(state):
    if ABBR_RE.match(state):
        return process.extractOne(state, STATE_ABBREVS)[0]
    else:
        return process.extractOne(state, STATES)[0]


def _lookup_county(county):
    known_counties = [x.county for x in APNS]
    return process.extractOne(county, known_counties)[0]


def lookup(state, county=None):
    if county and state is None:
        raise Exception("Lookup Error: Need to specify what state the county resides in.")
    found_state = _lookup_state(state)
    if not found_state:
        raise Exception("Unable to find a state for: {}".format(state))
    if county:
        county = _lookup_county(county)
    return _find_by_state_county(found_state, county)


__load_data()
