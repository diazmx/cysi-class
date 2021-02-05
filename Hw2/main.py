from huffman import *
from two import *
import string
import re
import math
import matplotlib.pyplot as plt
import numpy as np
import os


def readfile(f):
    """
    Read and convert a file to string
    """
    msg = ""
    flines = f.readlines()
    for line in flines:
        msg += line.replace('\n', "")
    return msg


def main_asd(remove_punctuation=False):
    # Read every text
    f = open("textos/txtmil.txt", 'r')
    txt1 = readfile(f)
    f = open('textos/txtdiezmil.txt', 'r')
    txt2 = readfile(f)
    f = open('textos/txtcincuenta.txt', 'r')
    txt3 = readfile(f)
    txt_list = [txt1, txt2, txt3]

    # Remove punctuation and numbers
    if remove_punctuation:
        new = list()
        for t in txt_list:
            new.append(clean_text(t))
        txt_list = new
        print("Texto limpo")

    # Count frecuency
    frec_list = list()
    for t in txt_list:
        frec_list.append(count_frecuency(t))
    print("Frecuencias calculadas")

    # Get Huffman Codes
    hcodes_list = list()
    for f in frec_list:
        hcodes_list.append(convert_to_treelist(f))
    print("Codigos calculados")

    # Encoding every text and open new file to save
    # statistics and dictionary
    data_out_txt1 = open("salida/data_txt1.txt", 'w')
    data_out_txt2 = open("salida/data_txt2.txt", 'w')
    data_out_txt3 = open("salida/data_txt3.txt", 'w')
    files_list = [data_out_txt1, data_out_txt2, data_out_txt3]
    # Print dictionarys
    for fi, hcodes in zip(files_list, hcodes_list):
        fi.write("Diccionario:\n")
        for elem in hcodes:
            fi.write(str(elem)+'\n')
        fi.write("=====================\n")
    print("Codigos impresos")

    # Statistics
    ngrams = 5
    for frec, msg, fil in zip(frec_list, txt_list, files_list):
        activity_two(frec, msg, ngrams, fil)
    print("Estadisticas completadas")

    # Generete a new key
    # generate_key(256)
    # Encode new message
    encode_openssl('aes', 'textos/txtmil.txt',
                   'openssl/enc_txtmil_aes.enc', 'llaves/llave-256.key')
    # Decode new message
    decode_openssl('aes', 'openssl/enc_txtmil_aes.enc',
                   'openssl/dec_txtmil_aes.dec', 'llaves/llave-256.key')


def generate_key(n):
    """
    Generate a new key with n bits.

    Parameters
    ----------
    n : int
    """
    cmd = "openssl rand -hex "+str(int(n/8))+" > llaves/llave-"+str(n)+".key"
    os.system(cmd)
    print("Llave generada correctamente")


def encode_openssl(algorithm, in_file_name, out_file_name, key_file_name):
    """
    Encode a new message with openssl.

    Parameters
    ----------
    algorithm       : str des3 | aes
    in_file_name    : str name of input file  
    out_file_name   : str name of output file
    key_file_name   : str name of key file
    """
    if algorithm == 'des3':
        cmd = 'openssl des3 -e -in '+in_file_name + \
            " -out "+out_file_name+" -kfile "+key_file_name
    else:
        cmd = 'openssl AES-256-CFB -e -in '+in_file_name + \
            " -out "+out_file_name+" -kfile "+key_file_name
    os.system(cmd)
    print("Texto Encriptado con "+algorithm)


def decode_openssl(algorithm, in_file_name, out_file_name, key_file_name):
    """
    Decode a encode message with openssl.

    Parameters
    ----------
    algorithm       : str des3 | aes
    in_file_name    : str name of input file  
    out_file_name   : str name of output file
    key_file_name   : str name of key file
    """
    if algorithm == 'des3':
        cmd = 'openssl des3 -d -in '+in_file_name + \
            " -out "+out_file_name+" -kfile "+key_file_name
    else:
        cmd = 'openssl AES-256-CFB -d -in '+in_file_name + \
            " -out "+out_file_name+" -kfile "+key_file_name
    os.system(cmd)
    print("Texto Desencriptado con "+algorithm)


def clean_text(s, space=True):
    """
    Convert to lower, remove punctiation and numbers.

    Parameters
    ----------
    s : str

    Returns
    -------
    str
    """
    s = s.lower()
    table = str.maketrans(dict.fromkeys(string.punctuation))
    s = s.translate(table)
    table = str.maketrans(dict.fromkeys(string.digits))
    s = s.translate(table)
    s = s.replace('«', '')
    s = s.replace('¿', '')
    s = s.replace('»', '')
    s = s.replace('¡', '')
    s = s.replace('á', 'a')
    s = s.replace('é', 'e')
    s = s.replace('í', 'i')
    s = s.replace('ó', 'o')
    s = s.replace('ú', 'u')
    if not space:
        s = s.replace(' ', '')
    return s


def main_two():
    f = open("in.txt", "r")
    msg = readfile(f)
    msg = msg.lower()

    # Parte 2: Lee el archivo con el libro
    fbook = open("book.txt", 'r')
    text_book = readfile(fbook)

    frec_list = count_frecuency(msg)
    h_codes = convert_to_treelist(frec_list)

    bits_text = coding(msg, h_codes)
    write_binary_file(bits_text)
    print("binary file done!")
    read_bin = read_binary_file()
    print(bits_text, len(bits_text))
    print(read_bin, len(read_bin))
    test2 = decoding(read_bin, h_codes)
    # print("Decodificación : ", test2)
    f_out = open("decod.txt", "w")
    f_out.write(test2)
    f_out.close()


def write_binary_file(s):
    i = 0
    buffer = bytearray()
    while i < len(s):
        buffer.append(int(s[i:i+8], 2))
        i += 8

    # now write your buffer to a file
    print(buffer)
    with open("binary_file.bin", "bw") as f:
        f.write(buffer)

    f.close()


def read_binary_file():
    with open("binary_file.bin", "rb") as f:
        test = bytearray(f.read())
    s = str()
    for i in test:
        #s += "{0:b}".format(i)
        s += get_bin(i, 8)
    return s


def get_bin(x, n=0):
    """
    Get the binary representation of x.

    Parameters
    ----------
    x : int
    n : int
        Minimum number of digits. If x needs less digits in binary, the rest
        is filled with zeros.

    Returns
    -------
    str
    """
    return format(x, 'b').zfill(n)


if __name__ == "__main__":
    main_asd(True)
