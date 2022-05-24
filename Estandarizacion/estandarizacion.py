import numpy as np
import pandas as pd

def promedio(array):
    suma = 0
    for i in array:
        suma += i

    suma /= len(array)
    return suma


def desv_estandar(array, prom):
    suma = 0
    for i in array:
        suma += (i - prom)**2

    suma /= len(array)
    suma = suma**0.5
    return suma


def x_estandar(array, prom, desv):
    x = []
    for i in array:
        if(desv == 0):
            x.append(0)
            continue
        a = round((i - prom)/desv, 4)
        x.append(a)

    return(x)


def estandarizacion(tabla):
    newTable = []
    for t in tabla:
        i = t[0]
        # print("\n\nVector: ", i)
        prom = promedio(i)
        desv = desv_estandar(i, prom)
        xEst = x_estandar(i, prom, desv)

        # print("Promedio:    ", prom)
        # print("Desviacion:  ", desv)
        # print("X Estandar:  ", xEst)
        newTable.append(xEst)
    
    pd.DataFrame(newTable).to_csv('estandarizacion.csv', index=False, header=None)

