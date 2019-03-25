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
    if sys.argv[1] not in capital_cities.values():
        print('Unknown capital city')
        return
    state_val = ""
    for key, val in capital_cities.items():
        if val == sys.argv[1]:
            state_val = key
            break
    for key, val in states.items():
        if val == state_val:
            print(key)
            break

if __name__ == '__main__':
    main()