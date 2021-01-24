from huffman import *
import string
import re


def readfile(f):
    """
    Read and convert a file to string
    """
    msg = ""
    flines = f.readlines()
    for line in flines:
        msg += line.replace('\n', " ")
    return msg


def check_frecuency_book(st):
    # Clean text
    st = st.lower()
    table = str.maketrans(dict.fromkeys(string.punctuation))
    new_s = st.translate(table)
    table = str.maketrans(dict.fromkeys(string.digits))
    new_s = new_s.translate(table)
    new_s = new_s.replace("í", "i")
    new_s = new_s.replace("ó", "o")
    new_s = new_s.replace("á", "a")
    new_s = new_s.replace("é", "e")
    new_s = new_s.replace("ú", "u")
    new_s = new_s.replace('\ufeff', "")
    new_s = new_s.replace('«', "")
    new_s = new_s.replace(' ', "")
    new_s = new_s.replace('̈', "")
    new_s = new_s.replace('̀', "")
    new_s = new_s.replace('̃', "")
    frec_letters = count_frecuency(new_s)
    print(frec_letters)
    #o_frec = open("frec_book.txt", "w")
    for key, value in sorted(frec_letters):
        print(key, value*100)


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

    # PArte 2
    fbook = open("book.txt", 'r')
    text_book = readfile(fbook)
    check_frecuency_book(text_book)


if __name__ == "__main__":
    main()
