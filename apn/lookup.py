

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