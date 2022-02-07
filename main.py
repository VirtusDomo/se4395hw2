#   Created by: James Anyabine
#
#
#
#

import os
import sys
import math
from nltk.book import *


def reader(filepath):
    #print("\nUsing method 1")

    with open(os.path.join(os.getcwd(), filepath), 'r') as f:
        # text_in = f.read()
        lines = [line for line in f.readlines()]
    return lines


def lexdiv(lines):
    unique = set()
    tokens = [[l.lower() for l in sublines] for sublines in lines]
    for list in lines:
        for item in list:
            unique.add(item)
    diversity = float(len(unique))/float(len(tokens))
    #print(len(unique), len(tokens))
    formal = '{:.2f}'.format(diversity)
    return formal


def preprocess(lines):

    return 0


def main():
    if len(sys.argv) > 1:
        rp = sys.argv[1]
        listed = reader(rp)
        div = lexdiv(listed)
        print(div)
        #print(listed)
    else:
        print('Error, insufficient path please retry.')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


