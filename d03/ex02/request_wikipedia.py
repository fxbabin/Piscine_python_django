#! /usr/bin/python3
 


import requests
import sys
import json
import dewiki

def main():
    if len(sys.argv) != 2:
        print("error")
        return
    title = sys.argv[1]
    url = 'https://en.wikipedia.org/w/api.php'
    arguments = {'action':'query', 'prop':'revisions', 'rvprop':'content', 'format':'json', 'titles':title}
    response = requests.get(url,params=arguments)
    if response.status_code != 200:
        print("Error : waiting status code 200 and "
              "received '{}' as status code".format(response.status_code))
        return
    res = response.json()
    if not res.get('query'):
        print("Error : could not find 'query' in response.")
        return
    if not res['query'].get('pages'):
        print("Error : could not find 'pages' in response['query'].")
        return
    #print(res)
    content = ""
    for page in res['query']['pages']:
        page_content = res['query']['pages'][page]
        if not page_content['revisions'][0].get('*'):
            return
        content += "{}\n".format(page_content['revisions'][0]['*'])
    file_name = title.replace(" ", "_")
    with open(file_name+".wiki", 'w') as out_file:
        out_file.write(dewiki.from_string(content))

if __name__ == '__main__':
    main()