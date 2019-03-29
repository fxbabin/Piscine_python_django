#! /usr/bin/python3

import sys
import requests
from bs4 import BeautifulSoup

def send_themeuest(theme):
    #  print(theme)
    #  game, house, monogamy
    response = requests.get('https://en.wikipedia.org/wiki/' + theme)
    if response.status_code == 404:
        print("It leads to a dead end !")
        sys.exit(0)
    if response.status_code != 200:
        print("Error in themeuest : '{}' code returned".format(str(response.status_code)))
        sys.exit(0)
    soup = BeautifulSoup(response.content, 'html.parser')
    relevant_content = soup.find(id="mw-content-text")
    curr_p = False
    tmp = None
    for el in relevant_content.find_all('p'):
        if el.b:
            curr_p = True
            tmp = el
            break
            print(el.b)
    if not curr_p:
        print("It leads to a dead end !")
        sys.exit(0)
    all_a = tmp.find_all('a')
    if len(all_a) == 0:
        print("It leads to a dead end !")
        sys.exit(0)
    for a in all_a:
        if not a['href'].startswith('/wiki'):
            continue
        if a['href'].startswith('/wiki/Help'):
            continue
        theme = a['href'][6:]
        return (theme.replace("_", " "))

def process_request(theme):
    roads = [theme]
    while (theme.lower() != 'philosophy'):
        theme = send_themeuest(theme)
        if theme is None:
            print("It leads to a dead end !")
            sys.exit(0)
        if theme in roads:
            print('It leads to an infinite loop !')
            sys.exit(0)
        roads.append(theme)
    for road in roads:
        print(road)
    return (len(roads))


def main():
    if len(sys.argv) != 2:
        print("Error : wrong number of arguments")
        return
    len_road = process_request(sys.argv[1])
    print("{} roads from {} to philosophy".format(len_road, sys.argv[1]))



if __name__ == '__main__':
    main()
