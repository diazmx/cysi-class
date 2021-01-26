import math
from nltk import everygrams


def activity_two(frec_letters, msg):
    R = math.log(len(frec_letters), 2)
    print("Rango absoluto R = ", R)

    grams = list(everygrams(msg.lower(), 2, 2))
    realgram = list(set(grams))
    # print(len(realgram))
    r = rango(2, len(realgram))
    print("rango r = ", r)

    # Redundancia para cada n
    D = R - r
    print("Redundancia D = ", D)

    # Cantidad de información de cada char
    # ademas de entroopia
    entropia = 0
    print("Bits de informacion para cada simbolo")
    for key, frec in frec_letters:
        bit_info = math.log2(1/frec)
        print(key, bit_info)
        entropia += (frec * bit_info)

    print("Entropia = ", entropia)


def create_digrama(keys):
    """
    Functions to create cronogram
    """
    l_grams = []
    for i in keys:
        pre = i[0]
        for j in keys:
            l_grams.append((pre, j[0]))
    return l_grams


def create_trigrama(keys):
    """
    Functions to create cronogram
    """
    l_grams = []
    for i in keys:
        pre = i[0]
        for j in keys:
            mid = j[0]
            for k in keys:
                l_grams.append((pre, mid, k[0]))
    return l_grams


def count_occurences(poligram, realgram):
    count_oc = 0
    for gram in poligram:
        for key in realgram:
            if gram == key:
                count_oc += 1
    return count_oc


def rango(N, occurencias):
    return math.log(occurencias, 2**N)
