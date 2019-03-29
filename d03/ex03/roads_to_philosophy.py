#! /usr/bin/python3

import sys
import requests
from bs4 import BeautifulSoup

def send_request(theme):
    print(theme)
    response = requests.get('https://en.wikipedia.org/wiki/' + theme)
    if response.status_code == 404:
        print("0 It leads to a dead end !")
        sys.exit(0)
    if response.status_code != 200:
        print("Error in request : '{}' code returned".format(str(response.status_code)))
        sys.exit(0)
    soup = BeautifulSoup(response.content, 'html.parser')
    relevant_content = soup.find(id="mw-content-text")
    curr_p = False
    for el in relevant_content.find_all('p'):
        
        if el.b:
            curr_p = True
            break
            print(el.b)
            #curr_p = el
    #print(el)
    if not curr_p:
        print("1 It leads to a dead end !")
        sys.exit(0)
    all_a = relevant_content.find_all('a')
    if len(all_a) == 0:
        print("2 It leads to a dead end !")
        sys.exit(0)
    #print(all_a)
    for a in all_a:
        # if not a['href'].startswith('/wiki'):
        #     continue
        # if a['href'].startswith('/wiki/Help'):
        #     continue
        # req = a['href'][6:]
        # return (req)
        if str(a).find('title') > 0:
            target = a['title']
            if target:
                if not target.startswith('Help:'):
                    print(a) 
                    return target

        #if a.startswith("/wiki") and not a.startswith("/wiki/Help"):
        #    print(a[6:])
    #title = str(soup.title.string).replace(" - Wikipedia", "")
    #print(rr)
    #exit(1)

def process_request(req):
    roads = [req]
    while (req.lower() != 'philosophy'):
        req = send_request(req)
        # if req is None:
        #     print('It leads to an infinite loop !')
        #     exit(1)
        if req in roads: # requete deja trouvee
            #print("debug : req = ", req)
            print('It leads to an infinite loop !')
            exit(1)
        roads.append(req)
    for road in roads:
        print(road)

def main():
    if len(sys.argv) != 2:
        print("Error : wrong number of arguments")
        return
    process_request(sys.argv[1])

if __name__ == '__main__':
    main()
