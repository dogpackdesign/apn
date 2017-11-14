#######################################
#
# apn - library to look up formats for
# APN in a given state/county
#
#######################################

import argparse

import apn


def lookup(args):
    if args['list']:
        return [x.serialize for x in apn.APNS]

    return apn.lookup(args['state'], args['county'])


def get_parser():
    parser = argparse.ArgumentParser(description='Look up APN format by State and/or County')
    parser.add_argument('-s', '--state', type=str, help='US state to lookup APN format')
    parser.add_argument('-c', '--county', type=str, help='by specific county')
    parser.add_argument('-l', '--list', help='list all APNs', action='store_true')
    parser.add_argument('-v', '--version', help='current version', action='store_true')
    return parser


def runner():
    parser = get_parser()
    args = vars(parser.parse_args())

    if args['version']:
        print(apn.__version__)
        return
    if not args['state'] and not args['county'] and not args['list']:
        parser.print_help()
        return
    else:
        print(lookup(args))


if __name__ == '__main__':
    runner()
