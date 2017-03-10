import re
import json


def main():
    regex_convert()


def regex_convert():
    with open("formats.json", "r") as jsonfile:
        apnjson = json.load(jsonfile)
        apns = apnjson["root"]

    chars = []
    for state, data in apns.iteritems():
        for county, values in data.items():
            regex = []
            for f in values["formats"]:
                pattern = ""
                hold = ""
                count = 1
                for c in range(0, len(f)):
                    if f[c] == hold:
                        count += 1
                    else:
                        if hold == "":
                            pass
                        else:
                            pattern = char_text(hold, pattern)
                            if count > 1:
                                pattern += "{" + str(count) + "}"
                            else:
                                pass
                        hold = f[c]
                        count = 1

                    if c == len(f) - 1:
                        pattern = char_text(hold, pattern)
                        if count > 1:
                            pattern += "{" + str(count) + "}"
                        else:
                            pass
                    else:
                        pass
                regex.append(pattern)
                print pattern
            apns[state][county]["regex"] = regex
            if len(values["formats"]) > 0:
                if values["formats"][0] == "none":
                    apns[state][county]["formats"] = []
                    apns[state][county]["regex"] = []
                else:
                    pass
            else:
                pass
    with open("regex.json", "w") as newjson:
        json.dump(apns, newjson)


def char_text(hold, pattern):
    if hold == "X":
        pattern += "\d"
    elif hold == "A":
        pattern += "[A-Z]"
    elif hold == "S":
        pattern += "\s"
    else:
        pattern += hold
    return pattern


if __name__ == "__main__":
    main()
