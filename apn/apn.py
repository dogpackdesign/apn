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
    results = []
    for obj in APNS:
        if state:
            if obj.state_abbrev == state or obj.state == state:
                if county:
                    if obj.county == county:
                        results.append(obj.apn_format)
                        print obj.state, obj.county, obj.apn_format
                    else:
                        pass
                else:
                    results.append(obj.apn_format)
                    print obj.state, obj.county, obj.apn_format
            else:
                pass
        else:
            results.append(obj.apn_format)
            print obj.state, obj.county, obj.apn_format
    return results


def validate(apn, state=None, county=None):
    if state:
        if county:
            pass
        else:
            pass
    else:
        pass
    return


load_apns()
