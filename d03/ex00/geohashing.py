#! /usr/bin/python3

import sys
from antigravity import geohash

def main():
    if (len(sys.argv) != 5):
        print ("Error : wrong number of arguments for geohashing.\n"
               "waiting following arguments:\n"
               "- latitude (ex: 37.421542)\n"
               "- longitude (ex: -122.085589)\n"
               "- date (ex : 2005-05-26)\n"
               "- dow (ex: 10458.68)\n")
        return
    try:
        latitude = float(sys.argv[1])
        longitude = float(sys.argv[2])
        date = sys.argv[3]
        dow = float(sys.argv[4])
    except ValueError:
        print("Error : wrong type for latitude, longitude or dow")
        return
    tmp = "{}-{}".format(date, dow).encode('ascii')
    geohash(latitude, longitude, tmp)

if __name__ == '__main__':
    main()