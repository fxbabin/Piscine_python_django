#! /usr/bin/python3

import sys

def print_header(file):
    file.write("<!DOCTYPE html>\n<html lang=\"en\">\n\t<head>\n\t\t<meta charset=\"utf-8\"/>\n\t\t<title>periodic table</title>\n\t</head>\n\t<body>\n")

def print_end(file):
    file.write("\t</body>\n</html>")

def print_line(out_file, periodic_table, space_1=0, nb_elem_1=0, space_2=0, nb_elem_2=0, space_3=0):
    out_file.write("\t\t\t<tr>\n")
    pos = 0
    for _ in range(space_1):
        out_file.write("\t\t\t\t<td></td>\n")
    
    for _ in range(nb_elem_1):
        out_file.write("\t\t\t\t<td style=\"border: 1px solid black; padding: 10px\">\n")
        out_file.write("\t\t\t\t<h4>{}</h4>\n".format(periodic_table[pos]["element"]))
        out_file.write("\t\t\t\t\t<ul>\n")
        out_file.write("\t\t\t\t\t\t<li>{}</li>\n".format(periodic_table[pos]["atom_num"]))
        out_file.write("\t\t\t\t\t\t<li>{}</li>\n".format(periodic_table[pos]["symbol"]))
        out_file.write("\t\t\t\t\t\t<li>{}</li>\n".format(periodic_table[pos]["mass"]))
        out_file.write("\t\t\t\t\t</ul>\n")
        out_file.write("\t\t\t\t</td>\n")
        pos += 1
    
    for _ in range(space_2):
        out_file.write("\t\t\t\t<td></td>\n")
    
    for _ in range(nb_elem_2):
        out_file.write("\t\t\t\t<td style=\"border: 1px solid black; padding: 10px\">\n")
        out_file.write("\t\t\t\t<h4>{}</h4>\n".format(periodic_table[pos]["element"]))
        out_file.write("\t\t\t\t\t<ul>\n")
        out_file.write("\t\t\t\t\t\t<li>{}</li>\n".format(periodic_table[pos]["atom_num"]))
        out_file.write("\t\t\t\t\t\t<li>{}</li>\n".format(periodic_table[pos]["symbol"]))
        out_file.write("\t\t\t\t\t\t<li>{}</li>\n".format(periodic_table[pos]["mass"]))
        out_file.write("\t\t\t\t\t</ul>\n")
        out_file.write("\t\t\t\t</td>\n")
        pos += 1
    
    for _ in range(space_3):
        out_file.write("\t\t\t\t<td></td>\n")
    out_file.write("\t\t\t</tr>\n")

def main():
    periodic_table = []
    with open('periodic_table.txt', 'r') as in_file:
        for line in in_file:

            line_split = line.strip().split(',')
            element = line_split[0].split('=')[0].strip()
            atom_num = line_split[1].split(':')[1]
            symbol = line_split[2].split(':')[1].strip()
            mass = line_split[3].split(':')[1]
            tmp = {}
            #if element not in periodic_table:
            tmp["element"] = element
            tmp["atom_num"] = atom_num
            tmp["symbol"] = symbol
            tmp["mass"] = mass
            periodic_table.append(tmp)

    with open('periodic_table.html', 'w') as out_file:
        print_header(out_file)
        out_file.write("\t\t<table>\n")
        print_line(out_file, periodic_table[0:2], nb_elem_1=1, space_2=15, nb_elem_2=1)
        print_line(out_file, periodic_table[2:10], nb_elem_1=2, space_2=9, nb_elem_2=6)
        print_line(out_file, periodic_table[10:19], nb_elem_1=2, space_2=9, nb_elem_2=6)
        print_line(out_file, periodic_table[19:37], nb_elem_1=17)
        print_line(out_file, periodic_table[37:54], nb_elem_1=17)
        print_line(out_file, periodic_table[54:71], nb_elem_1=17)
        print_line(out_file, periodic_table[71:88], nb_elem_1=17)
        out_file.write("\t\t</table>\n")
        print_end(out_file)
    



if __name__ == '__main__':
    main()