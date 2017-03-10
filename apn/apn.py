import pickle
import re

from pkg_resources import resource_stream

APNS = []
ABBR_RE = re.compile(r'^[a-zA-Z]{2}$')


class Apn(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __repr__(self):
        return "<APN:%s>" % self.apn_format

    def __str__(self):
        return self.apn_format


def load_apns():
    with resource_stream(__name__, 'apns.pkl') as pklfile:
        for s in pickle.load(pklfile):
            apn = Apn(**s)
            APNS.append(apn)


def lookup(state=None, county=None):
    if state is None or county is None:
        print "lookup() requires state and county"
    else:
        for obj in APNS:
            if obj.state_abbr == state:
                print obj


load_apns()
