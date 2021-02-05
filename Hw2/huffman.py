from collections import Counter
from tree import *


def readfile(f):
    """
    Read and convert a file to string
    """
    h_codes = []
    flines = f.readlines()
    for line in flines:
        h_codes.append(line.replace('\n', '').split('\t'))
    return h_codes


def count_frecuency(msg):
    """
    Function to count the frecuency of every symbol. 
    Return List Data Structure with frecuency.
    """
    tam = len(msg)
    is_one = 0
    dictlist = []
    # Use Count for count every char in msg, then convert to dict
    count = dict(Counter(msg))
    for key, value in count.items():
        temp = [key, value/tam]
        dictlist.append(temp)
    # Sort list by index 1
    dictlist.sort(key=lambda dictlist: dictlist[1])
    return dictlist


def convert_to_treelist(list_):
    """
    Function to covert a simple list to a TreeList
    """
    tlist = TreeList()
    tlist.create(list_)
    tlist.complete()
    tlist.print_tree(tlist.head.next.tree, "")
    tlist.close_file()
    #print("\nCodigos generados en archivo 'out.txt'")
    o = open("out.txt", "r")
    h_codes = readfile(o)
    # print(h_codes)
    return h_codes


def coding(input_str, huffman_codes):
    c_str = ""
    for key in input_str:
        for par in huffman_codes:
            if key == par[0]:
                c_str += par[1]
    return c_str


def decoding(input_str, huffman_codes):
    d_str = ""
    first = 0
    last = 1
    tam = len(input_str)
    while first < tam:
        for par in huffman_codes:
            if input_str[first:last] == par[1]:
                d_str += par[0]
                first = last
                last = first
        last += 1
    return d_str
