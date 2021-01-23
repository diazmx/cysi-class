from huffman import *


def readfile(f):
    """
    Read and convert a file to string
    """
    msg = ""
    flines = f.readlines()
    for line in flines:
        msg += line.replace('\n', " ")
    return msg


def main():
    f = open("in.txt", "r")
    msg = readfile(f)
    print(msg)
    frec_list = count_frecuency(msg)
    h_codes = convert_to_treelist(frec_list)
    test = coding(msg, h_codes)
    print(test)
    test2 = decoding(test, h_codes)
    print(test2)


if __name__ == "__main__":
    main()
