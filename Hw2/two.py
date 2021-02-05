import math
from nltk import everygrams
import matplotlib.pyplot as plt
import numpy as np


def activity_two(frec_letters, msg, n_grams, fil):

    R = math.log(len(frec_letters), 2)
    #print("\nRango absoluto R = ", R)
    fil.write("\nRango absoluto R = " + str(R))

    # Creamos diferentes gramas
    grams = list(everygrams(msg, n_grams, n_grams))
    # Convertirmos a "set" para quitar elementos repetidos
    realgram = list(set(grams))

    # Calcular rangos r
    rangos_grams = graficar_rangos(n_grams+1, msg.lower(), R)
    # Imprimar los rangos
    # print("\nrangos 'r' para cada n-gram")
    fil.write("\nrangos 'r' para cada n-gram")
    for i in range(n_grams):
        fil.write("\n\tn-gram[" + str(i+1) + "] - R = "+str(rangos_grams[i]))
        # print("n-gram[", i+1, "] - R =", rangos_grams[i])

    # Redundancia para cada n
    #print("\nRedundancia 'D' para cada rango 'r'")
    fil.write("\nRedundancia 'D' para cada rango 'r'")
    for i in range(n_grams):
        fil.write("\n\tn-gram[" + str(i+1) + "] - D = " +
                  str(R-rangos_grams[i]))
        # print("n-gram[", i+1, "] - D =", R-rangos_grams[i])

    # Cantidad de información de cada char
    # ademas de entroopia
    entropia = 0
    fil.write("\nBits de informacion para cada simbolo\n")
    for key, frec in frec_letters:
        bit_info = math.log2(1/frec)
        #print(key, bit_info)
        fil.write(""+str(key)+" - "+str(bit_info)+"\n")
        entropia += (frec * bit_info)
    fil.write("\nEntropia = " + str(entropia))
    #print("\nEntropia = " + str(entropia))


def graficar_rangos(max_rango, msg, R):
    lis_values_rangos = []
    for i in range(1, max_rango):
        # Creamos diferentes gramas
        grams = list(everygrams(msg, i, i))
        # Convertirmos a "set" para quitar elementos repetidos
        realgram = list(set(grams))
        # print(realgram)
        r = math.log(len(realgram), 2**i)
        lis_values_rangos.append(r)
    return lis_values_rangos
