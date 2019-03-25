#! /usr/bin/python3

import sys


def main():
    states = {
        "Oregon"    : "OR",
        "Alabama"   : "AL",
        "New Jersey": "NJ",
        "Colorado"  : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    if len(sys.argv) != 2:
        return
    if sys.argv[1] not in states:
        print('Unknown state')
        return
    print(capital_cities[states[sys.argv[1]]])


if __name__ == '__main__':
    main()