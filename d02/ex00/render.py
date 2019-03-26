#! /usr/bin/python3

import sys, os, re


def check_file(file_name, extension):
    ext = file_name.split('.')[1]
    if ext != extension:
        print("Error : '{}' has a wrong file extension (wanting '{}').".format(file_name, extension))
        return (False)
    exists = os.path.isfile(file_name)
    if not exists:
        print("Error : '{}' does not exists.".format(file_name))
        return (False)
    return (True)

def setting_parser():
    try:
        settings = {}
        with open("settings.py", 'r') as in_file:
            for line in in_file:
                line_split = line.split('=')
                matches = re.search(r'".*"', line_split[1])
                res = matches.group()[1:-1]
                settings[line_split[0].strip()] = res.strip()
            return (settings)
    except Exception as e:
        print(e)
        return ({})

def apply_settings(file_name, settings):
    try:
        with open(file_name.split('.')[0] + ".html", "w") as out_file:
            with open(file_name, 'r') as in_file:
                for line in in_file:
                    matches = re.findall(r'{.*?}', line)
                    if not matches:
                        out_file.write(line)
                        continue
                    res = line
                    for match in matches:
                        res = re.sub(match, settings[match[1:-1]], res)
                    out_file.write(res)
    except Exception as e:
        print(e)

def main():
    if len(sys.argv) != 2:
        print ('Error : wrong number of arguments')
        return
    if not check_file(sys.argv[1], "template"):
        return
    if not check_file("settings.py", "py"):
        return
    settings = setting_parser()
    if not settings:
        return
    apply_settings(sys.argv[1], settings)

if __name__ == '__main__':
    main()