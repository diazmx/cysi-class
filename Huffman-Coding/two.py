import math
from nltk import everygrams
import matplotlib.pyplot as plt
import numpy as np


def activity_two(frec_letters, msg, n_grams):

    R = math.log(len(frec_letters), 2)
    print("\nRango absoluto R = ", R)
    # Creamos diferentes gramas
    grams = list(everygrams(msg.lower(), n_grams, n_grams))
    # Convertirmos a "set" para quitar elementos repetidos
    realgram = list(set(grams))

    # Calcular rangos r
    rangos_grams = graficar_rangos(n_grams+1, msg.lower(), R)
    # Imprimar los rangos
    print("\nrangos 'r' para cada n-gram")
    for i in range(n_grams):
        print("n-gram[", i+1, "] - R =", rangos_grams[i])

    # Redundancia para cada n
    print("\nRedundancia 'D' para cada rango 'r'")
    for i in range(n_grams):
        print("n-gram[", i+1, "] - D =", R-rangos_grams[i])

    print("\nObservar figura 'grafica_rango.png'")
    # Cantidad de información de cada char
    # ademas de entroopia
    entropia = 0
    print("\nBits de informacion para cada simbolo")
    for key, frec in frec_letters:
        bit_info = math.log2(1/frec)
        print(key, bit_info)
        entropia += (frec * bit_info)
    print("\nEntropia = ", entropia)


def graficar_rangos(max_rango, msg, R):
    plt.close
    lis_values_rangos = []
    for i in range(1, max_rango):
        # Creamos diferentes gramas
        grams = list(everygrams(msg, i, i))
        # Convertirmos a "set" para quitar elementos repetidos
        realgram = list(set(grams))
        r = math.log(len(realgram), 2**i)
        lis_values_rangos.append(r)

    D = R - np.array(lis_values_rangos)
    plt.plot(list(range(1, max_rango)),
             lis_values_rangos, 'ro', label="rango r")
    plt.plot(list(range(1, max_rango)), D, 'bs', label="Redundancia D")
    plt.axis([0, max_rango, 0, 5])
    plt.xlabel("Poligramas")
    plt.legend()
    plt.savefig("grafica_rango.png")

    return lis_values_rangos
