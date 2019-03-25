#! /usr/bin/python3

import sys


def get_state_to_capital(states, capitals):
    state_to_capital = {}
    for state in states:
        state_to_capital[state] = capitals[states[state]]
    return (state_to_capital)

def get_capital_to_state(state_to_capital):
    capital_to_state = {}
    for state, capital in state_to_capital.items():
        capital_to_state[capital.lower()] = state
    return (capital_to_state)

def reformat_state_to_capital(state_to_capital):
    new = {}
    for state, capital in state_to_capital.items():
        new[state.lower()] = capital
    return (new)

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
    split = sys.argv[1].split(',')
    state_to_capital = get_state_to_capital(states, capital_cities)
    capital_to_state = get_capital_to_state(state_to_capital)
    state_to_capital = reformat_state_to_capital(state_to_capital)
    for elem in split:
        elem = elem.strip().lower()
        if len(elem) == 0:
            continue
        if elem in state_to_capital:
            capital = state_to_capital[elem]
            state = capital_to_state[capital.lower()]
            print("{} is the capital of {}".format(capital, state))
        elif elem in capital_to_state:
            state = capital_to_state[elem]
            capital = state_to_capital[state.lower()]
            print("{} is the capital of {}".format(capital, state))
        else:
            print("{} is neither a capital city not a state".format(elem))

if __name__ == '__main__':
    main()