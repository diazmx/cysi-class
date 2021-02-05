from huffman import *
from two import *
import string
import re
import math
import matplotlib.pyplot as plt
import numpy as np


def readfile(f):
    """
    Read and convert a file to string
    """
    msg = ""
    flines = f.readlines()
    for line in flines:
        msg += line.replace('\n', " ")
    return msg


def graficar_comparacion(compare_frec):
    # set width of bar
    monogram_frec = [['a', 10.60], ['b', 1.16], [
        'c', 3.54], ['d', 5.87], ['e', 13.11], ['f', 1.13], ['g', 1.40], ['h', 0.60], ['i', 7.16], ['j', 0.25], ['k', 0.11], ['l', 4.42], ['m', 3.11], ['n', 7.14], ['o', 8.23], ['p', 2.71], ['q', 0.74], ['r', 6.95], ['s', 8.47], ['t', 5.40], ['u', 4.34], ['v', 0.82], ['w', 0.12], ['x', 0.15], ['y', 0.79], ['z', 0.26], ['ñ', 0.10]]
    monogram_frec = np.array(monogram_frec)
    # set height of bar
    letras = compare_frec[:, 0]
    monog_frec = monogram_frec[:, 1].astype(np.float)
    mi_frec = compare_frec[:, 1].astype(np.float)

    x = np.arange(len(letras))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, monog_frec, width,
                    label='Frecuencia de Monograma')
    rects2 = ax.bar(x + width/2, mi_frec, width, label='Mi resultados')

    # Titles
    ax.set_ylabel('Frecuencia')
    ax.set_xticks(x)
    ax.set_xticklabels(letras)
    ax.legend()

    fig.tight_layout()

    plt.savefig("compara.png")
    plt.close()


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
    new_s = new_s.replace('̈', "")
    new_s = new_s.replace('̀', "")
    new_s = new_s.replace('̃', "")
    frec_letters = count_frecuency(new_s)
    compare_frec = []
    for key, value in sorted(frec_letters):
        compare_frec.append([key, float(value*100)])
    compare_frec = np.array(compare_frec)

    return frec_letters, new_s


def check_frecuency_book__without_space(st):
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
    compare_frec = []
    for key, value in sorted(frec_letters):
        compare_frec.append([key, float(value*100)])
    compare_frec = np.array(compare_frec)

    graficar_comparacion(compare_frec)

    return frec_letters, new_s


def main():
    f = open("in.txt", "r")
    msg = readfile(f)
    msg = msg.lower()

    # Parte 2: Lee el archivo con el libro
    fbook = open("book.txt", 'r')
    text_book = readfile(fbook)
    # Obtener la frecuencia con el string procesado
    f_letters, new_text_book = check_frecuency_book(msg)

    frec_list = count_frecuency(new_text_book)
    h_codes = convert_to_treelist(frec_list)
    # Mesaje para codificar
    # print("\nMensaje : ", new_text_book)
    f_out1 = open("mensaje.txt", "w")
    f_out1.write(new_text_book)
    f_out1.close()
    test = coding(new_text_book, h_codes)
    # print("Codificación : ", test)
    f_out2 = open("simbolos.txt", "w")
    f_out2.write(test)
    f_out2.close()
    test2 = decoding(test, h_codes)
    # print("Decodificación : ", test2)
    f_out = open("decod.txt", "w")
    f_out.write(test2)
    f_out.close()

    print()
    print("Parte 2")

    # Quitamos el espacio para compararlo con
    # la frecuencia de espanol si el espacio
    f_letters, new_text_book = check_frecuency_book__without_space(text_book)
    print("\nFrecuencia de Monogras - Comparación")
    print("Observar figura 'compara.png'")
    activity_two(f_letters, msg, 5)


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
    main_two()
