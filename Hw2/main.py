import codecs
from huffman import *
from two import *
import string
import re
import math
import matplotlib.pyplot as plt
import numpy as np
import os
from random import seed
from random import randint
import bitarray
ba = bitarray.bitarray()


def readfile(f):
    """
    Read and convert a file to string
    """
    msg = ""
    flines = f.readlines()
    for line in flines:
        msg += line.replace('\n', "")
    return msg


def step5(codificacion='UTF-8', errores='ignore'):
    txtlist_enc = list()
    # Read every text
    f = open("openssl/enc_txtmil_des3.enc", 'r',
             encoding=codificacion, errors=errores)
    txt = f.read()
    txtlist_enc.append(txt)
    f = open("openssl/enc_txtmil_aes.enc", 'r',
             encoding=codificacion, errors=errores)
    txt = f.read()
    txtlist_enc.append(txt)
    f = open("openssl/enc_txtdiezmil_des3.enc", 'r',
             encoding=codificacion, errors=errores)
    txt = f.read()
    txtlist_enc.append(txt)
    f = open("openssl/enc_txtdiezmil_aes.enc", 'r',
             encoding=codificacion, errors=errores)
    txt = f.read()
    txtlist_enc.append(txt)
    f = open("openssl/enc_txtcincuenta_des.enc",
             'r', encoding=codificacion, errors=errores)
    txt = f.read()
    txtlist_enc.append(txt)
    f = open("openssl/enc_txtcincuenta_aes.enc",
             'r', encoding=codificacion, errors=errores)
    txt = f.read()
    txtlist_enc.append(txt)

    # Count frecuency
    frec_list = list()
    for t in txtlist_enc:
        frec_list.append(count_frecuency(t))
    print("Frecuencias calculadas")

    # Get Huffman Codes
    hcodes_list = list()
    for f in frec_list:
        hcodes_list.append(convert_to_treelist(f))
    print("Codigos calculados")

    # Encoding every text and open new file to save
    # statistics and dictionary
    data_out_txt1 = open("openssl/data_txtmil_des.txt", 'w')
    data_out_txt2 = open("openssl/data_txtmil_aes.txt", 'w')
    data_out_txt3 = open("openssl/data_txtdiezmil_des.txt", 'w')
    data_out_txt4 = open("openssl/data_txtdiezmil_aes.txt", 'w')
    data_out_txt5 = open("openssl/data_txtcincuenta_des.txt", 'w')
    data_out_txt6 = open("openssl/data_txtcincuenta_aes.txt", 'w')
    files_list = [data_out_txt1, data_out_txt2, data_out_txt3,
                  data_out_txt4, data_out_txt5, data_out_txt6]
    # Print dictionarys
    for fi, hcodes in zip(files_list, hcodes_list):
        fi.write("Diccionario:\n")
        for elem in hcodes:
            fi.write(str(elem)+'\n')
        fi.write("=====================\n")
    print("Codigos impresos de codificacion")

    # Statistics
    ngrams = 5
    for frec, msg, fil in zip(frec_list, txtlist_enc, files_list):
        activity_two(frec, msg, ngrams, fil)
    print("Estadisticas completadas")


def step3(remove_punctuation=False):
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
            new.append(clean_text(t, False))
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
        for elem in sorted(hcodes):
            fi.write(str(elem)+'\n')
        fi.write("=====================\n")
    print("Codigos impresos")

    # Statistics
    ngrams = 5
    for frec, msg, fil in zip(frec_list, txt_list, files_list):
        activity_two(frec, msg, ngrams, fil)
    print("Estadisticas completadas")

    ##### Paso 5 #####
    # Aplicar las estadisticas a los textos cifrados


def openssl_functions(text=1, algorithm=1):
    # Generete a new key
    # generate_key(256)
    # Encode new message
    if text == 1:
        if algorithm == 1:
            encode_openssl('aes', 'textos/txtmil.txt',
                           'openssl/enc_txtmil_des3.enc', 'llaves/llave-128.key')
            # Decode new message
            decode_openssl('aes', 'openssl/enc_txtmil_des3.enc',
                           'openssl/dec_txtmil_des3.dec', 'llaves/llave-128.key')
        else:
            encode_openssl('aes', 'textos/txtmil.txt',
                           'openssl/enc_txtmil_aes.enc', 'llaves/llave-256.key')
            # Decode new message
            decode_openssl('aes', 'openssl/enc_txtmil_aes.enc',
                           'openssl/dec_txtmil_aes.dec', 'llaves/llave-256.key')
    elif text == 2:
        if algorithm == 1:
            encode_openssl('aes', 'textos/txtdiezmil.txt',
                           'openssl/enc_txtdiezmil_des3.enc', 'llaves/llave-128.key')
            # Decode new message
            decode_openssl('aes', 'openssl/enc_txtdiezmil_des3.enc',
                           'openssl/dec_txtdiezmil_des3.dec', 'llaves/llave-128.key')
        else:
            encode_openssl('aes', 'textos/txtdiezmil.txt',
                           'openssl/enc_txtdiezmil_aes.enc', 'llaves/llave-256.key')
            # Decode new message
            decode_openssl('aes', 'openssl/enc_txtdiezmil_aes.enc',
                           'openssl/dec_txtdiezmil_aes.dec', 'llaves/llave-256.key')
    else:
        if algorithm == 1:
            encode_openssl('aes', 'textos/txtcincuenta.txt',
                           'openssl/enc_txtcincuenta_des.enc', 'llaves/llave-128.key')
            # Decode new message
            decode_openssl('aes', 'openssl/enc_txtcincuenta_des.enc',
                           'openssl/dec_txtcincuenta_des.dec', 'llaves/llave-128.key')
        else:
            encode_openssl('aes', 'textos/txtcincuenta.txt',
                           'openssl/enc_txtcincuenta_aes.enc', 'llaves/llave-256.key')
            # Decode new message
            decode_openssl('aes', 'openssl/enc_txtcincuenta_aes.enc',
                           'openssl/dec_txtcincuenta_aes.dec', 'llaves/llave-256.key')


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


def paso8():
    text_instances = generate_msg(False)
    # convert_to_file(text_instances)
    # encode_instances()
    compare_bits(text_instances)


def compare_bits(text_instances, tipo='des'):
    list_bits_enc = list()
    if tipo == 'des':
        str_file = "paso8/enc/des/des-txt"
        j = 1
        for i in range(32):
            strfile = str_file + str(j) + ".enc"
            f = open(strfile, 'rb')
            txt = f.read()
            list_bits_enc.append(txt[8:])
            j += 1
            print(txt[8:])
        asdasd = list()
        for i in list_bits_enc:
            str_bits = str()
            for x in i:  # Convert bytes to bits
                # print(x, end=' ')
                str_bits += f'{x:08b}'
            asdasd.append(str_bits)
        for i in asdasd:
            print(i, len(i))
        print()


def encode_instances():
    # GEnerara criptograma des para cada file
    str_file_in = "paso8/txt"
    str_file_out = "paso8/enc/des/des-txt"
    j_in = 1
    for i in range(32):
        strfilein = str_file_in + str(j_in) + ".txt"
        strfileout = str_file_out + str(j_in) + ".enc"
        encode_openssl('des3', strfilein, strfileout, 'llaves/llave-128.key')
        j_in += 1

    # GEnerara criptograma des para cada file
    str_file_in = "paso8/txt"
    str_file_out = "paso8/enc/aes/aes-txt"
    j_in = 1
    for i in range(32):
        strfilein = str_file_in + str(j_in) + ".txt"
        strfileout = str_file_out + str(j_in) + ".enc"
        encode_openssl('aes', strfilein, strfileout, 'llaves/llave-256.key')
        j_in += 1


def convert_to_file(new_instances):
    str_file = "paso8/txt"
    j = 1
    for i in new_instances:
        strfile = str_file + str(j) + ".txt"
        f = open(strfile, 'w')
        f.write(str(bitstring_to_bytes(i))[2:-1])
        f.close()
        j += 1


def bitstring_to_bytes(s):
    return int(s, 2).to_bytes(-(-len(s) // 8), byteorder='big')


def generate_msg(random_msg=True, msg='Mi compu es roja'):
    """
    Return a list with 32 differents messages.

    Parameters
    ----------
    random_msg : bool
        Decistion to generate random message.
    msg: str
        Message to generate

    Returns
    -------
    list
        List with 32 differents messages.
    """
    if random_msg:
        # Generate a random msg
        print()
    else:
        if len(msg) == 16:  # Check if lenght of msg is 16 bytes
            arr_bytes = bytes(msg, 'utf-8')
            str_bits = str()
            for x in arr_bytes:  # Convert bytes to bits
                # print(x, end=' ')
                str_bits += f'{x:08b}'
            random_numers = generate_random_no_repeat()
            new_instances = list()
            new_instances.append(str_bits)
            for i in random_numers:
                temp_str = list(str_bits)
                if temp_str[i] == '0':
                    temp_str[i] = '1'
                else:
                    temp_str[i] = '0'
                new_instances.append("".join(temp_str))

            return new_instances
        else:
            print("Error: Please enter a message with 16 bytes!")


def generate_random_no_repeat():
    """
    Return a list with 31 unique and random integers.

    Parameters
    ----------
    Returns
    -------
    list
        List with 31 integers.
    """
    seed(1)
    new_rand = list()
    while len(new_rand) < 31:
        val = randint(0, 127)
        if val in new_rand:
            pass
        else:
            new_rand.append(val)
    print(len(new_rand))
    return new_rand


def hamming_distance(a, b):
    """
    Return Hamming Distance between two string of bytes.

    Parameters
    ----------
    a : str
        First string to compare.
    b : str
        Secodn string to compare.

    Returns
    -------
    int
        number of differents bits in common.
    Error
        string have differents lenghts.
    """
    res = 0
    if len(a) != len(b):
        return "Error: No son iguales"
    else:
        for i, j in zip(a, b):
            if i != j:
                res += 1
    return res


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
        # s += "{0:b}".format(i)
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
    # step3(True)
    # openssl_functions(3, 2)
    # paso8()
    step5(codificacion='latin-1')
    # paso8()
    # generate_key(128)
