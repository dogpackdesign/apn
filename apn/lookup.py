from apn import APNS


def lookup(state=None, county=None):
    if county and state is None:
        raise Exception("Lookup Error: Need to specify what state the county resides in.")
    else:
        if state:
            if county:
                results = {state: {county: []}}
                for obj in APNS:
                    if obj.state == state or obj.state_abbrev == state:
                        if obj.county == county:
                            results[state][county].append(obj.apn_format)
                        else:
                            pass
                    else:
                        pass
            else:
                results = {state: {}}
                for obj in APNS:
                    if obj.state == state or obj.state_abbrev == state:
                        if obj.county in results[state]:
                            results[state][obj.county].append(obj.apn_format)
                        else:
                            results[state][obj.county] = [obj.apn_format]
                    else:
                        pass
        else:
            results = {}
            for obj in APNS:
                if obj.state in results:
                    if obj.county in results[obj.state]:
                        results[obj.state][obj.county].append(obj.apn_format)
                    else:
                        results[obj.state][obj.county] = [obj.apn_format]
                else:
                    results[obj.state] = {obj.county: [obj.apn_format]}
        return results
