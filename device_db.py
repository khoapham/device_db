#!/usr/bin/env python3

import csv 
import sys

def main(argv):
    filename = argv[0]
    DeviceID = argv[1]
    print filename
    f = open(filename, 'r+')

    reader = csv.reader(f)
    for row in reader:
#        print row
#        print row[0]
#        print row[1]
        if DeviceID == row[0]:
            print "Device found:", row[1]

    f.close()

if __name__ == "__main__":
    main(sys.argv[1:])
