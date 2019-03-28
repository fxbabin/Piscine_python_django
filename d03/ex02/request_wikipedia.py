#! /usr/bin/python3

import requests
import sys
import json
import dewiki

def send_request(file_name, title):
    url = 'https://en.wikipedia.org/w/api.php'
    arguments = {'action':'query', 'prop':'revisions', 'rvprop':'content', 'format':'json', 'titles':title}
    response = requests.get(url,params=arguments)
    
    if response.status_code != 200:
        print("Error : waiting status code 200 and "
              "received '{}' as status code".format(response.status_code))
        return ("")
    
    res = response.json()
    
    if not res.get('query'):
        print("Error : could not find 'query' in response.")
        return ("")
    
    if not res['query'].get('pages'):
        print("Error : could not find 'pages' in response['query'].")
        return ("")

    content = ""
    for page in res['query']['pages']:
        page_content = res['query']['pages'][page]

        if not page_content.get('revisions'):
            print("Error : could not find 'revisions' in page_content.")
            return("")
        if not page_content['revisions'][0].get('*'):
            print("Error : could not find '*' in revisions.")
            return ("")
        content += "{}\n".format(page_content['revisions'][0]['*'])
    
    
    result = dewiki.from_string(content)
    tmp = str(result)[:9]
    
    if tmp == "#REDIRECT":
        redir = " ".join(str(result).split(' ')[1:]).strip()
        send_request(file_name, redir)
    else:
        with open(file_name+".wiki", 'w') as out_file:
            out_file.write(dewiki.from_string(result))
    return (result)

def main():
    if len(sys.argv) != 2:
        print("error")
        return
    file_name = sys.argv[1].replace(" ", "_")
    send_request(file_name, sys.argv[1])
    

if __name__ == '__main__':
    main()