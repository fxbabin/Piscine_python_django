#! /usr/bin/python3

import sys

def print_header(file):
    file.write("<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<meta charset=\"utf-8\"/>\n\t</head>\n\t<body>")

def print_end(file):
    file.write("\n\t</body>\n</html>")
#def print_style(file)

def main():
    periodic_table = {}
    with open('periodic_table.txt', 'r') as in_file:
        for line in in_file:

            line_split = line.strip().split(',')
            element = line_split[0].split('=')[0].strip()
            atom_num = line_split[1].split(':')[1]
            symbol = 
            print("element : {} ; atom_num : {}".format(element, atom_num))
    # with open('periodic_table.html', 'w') as out_file:
    #     print_header(out_file)
    #     print_end(out_file)



if __name__ == '__main__':
    main()