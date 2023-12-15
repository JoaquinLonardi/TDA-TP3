
import os
import random
import time
import numpy as np
import matplotlib.pyplot as plt
from algoritmo import leer_archivo
from programacion_lineal import hitting_set, hitting_set_bilardo
from scipy.optimize import curve_fit

PATH = 'sets_mediciones_exageradas_mas'
# Function to simulate your algorithm (replace with your actual algorithm)
def run_algorithm(input_file, aproximado=False):
    conjuntos = leer_archivo(input_file)
    U = set()
    for conjunto in conjuntos:
        U.update(conjunto, U)
    inicio = time.time()
    if not aproximado:
        size, max = hitting_set(conjuntos, U)
    else:
        size, max = hitting_set_bilardo(conjuntos)
    fin = time.time()

    return size, max, fin - inicio

# Create and run the algorithm on each test file, measuring run time
# files = [100, 150, 200, 300, 500, 750, 1000]
files = [10,20,30,40,50,60,70,80,90,100,200,500]
run_times = []
run_times_aprox = []
sizes_normales = []
sizes_aproximados = []
mayores = []
for i in range(0, len(files)):
    file_name = f"set{files[i]}.txt"
    # size, _ , time_exacto = run_algorithm(f"{PATH}/{file_name}")
    run_times.append(1)
    size_aproximado, mayor, time_aprox = run_algorithm(f"{PATH}/{file_name}", True)
    # print(f"Archivo número {files[i]}: {run_time}")
    run_times_aprox.append(time_aprox)
    sizes_normales.append(1)
    sizes_aproximados.append(size_aproximado)
    mayores.append(mayor)


with open("mediciones_pl_reentrega_EXAGERADOS_MAS_APROX.csv", mode="w") as file:
    file.write("Cantidad de conjuntos, medicion progamacion lineal normal, medicion programacion aproximada, valor normal, valor_aproximado, Mayor elemento, r(I)")
    file.write('\n')
    for i in range(0, len(files)):
        file.write(str(files[i]))
        file.write(',')
        file.write(str(run_times[i]))
        file.write(',')
        file.write(str(run_times_aprox[i]))
        file.write(',')
        file.write(str(sizes_normales[i]))
        file.write(',')
        file.write(str(sizes_aproximados[i]))
        file.write(',')
        file.write(str(mayores[i]))
        file.write(',')
        file.write(str(sizes_aproximados[i]/sizes_normales[i]))


        file.write('\n')


