
import os
import random
import time
import numpy as np
import matplotlib.pyplot as plt
from algoritmo import leer_archivo
from programacion_lineal import hitting_set, hitting_set_bilardo
from scipy.optimize import curve_fit

NUM_FILES = 20
# Function to simulate your algorithm (replace with your actual algorithm)
def run_algorithm(input_file, aproximado=False):
    conjuntos = leer_archivo(input_file)
    if not aproximado:
        size, max = hitting_set(conjuntos)
    else:
        size, max = hitting_set_bilardo(conjuntos)
    return size, max

# Create and run the algorithm on each test file, measuring run time
# files = [100, 150, 200, 300, 500, 750, 1000]
files = [10,20,30,40,50,60,70,80,90,100,200,500]
files = [100, 200, 300]
run_times = []
run_times_aprox = []
sizes_normales = []
sizes_aproximados = []
mayores = []
for i in range(0, len(files)):
    file_name = f"set{files[i]}.txt"
    inicio = time.time()
    size, _ = run_algorithm(f"sets_mediciones_comp_pl/{file_name}")
    fin = time.time()
    run_times.append(fin - inicio)
    inicio = time.time()
    size_aproximado, mayor = run_algorithm(f"sets_mediciones_comp_pl/{file_name}", True)
    fin = time.time()
    # print(f"Archivo número {files[i]}: {run_time}")
    run_times_aprox.append(fin - inicio)
    sizes_normales.append(size)
    sizes_aproximados.append(size_aproximado)
    mayores.append(mayor)

# with open("mediciones_grandes.csv", mode="w") as file:
#     file.write("Tamaño de archivo, medicion progamacion lineal normal, medicion programacion aproximada, Mayor elemento, r(I)")
#     file.write('\n')
#     for i in range(0, len(files)):
#         file.write(str(files[i]))
#         file.write(',')
#         file.write(str(sizes_normales[i]))
#         file.write(',')
#         file.write(str(sizes_aproximados[i]))
#         file.write(',')
#         file.write(str(mayores[i]))
#         file.write(',')
#         file.write(str(sizes_aproximados[i]/sizes_normales[i]))
#
#
#         file.write('\n')

with open("mediciones_exageradas.csv", mode="w") as file:
    file.write("Tamaño de universo, medicion progamacion lineal normal, medicion programacion aproximada, valor normal, valor_aproximado, Mayor elemento, r(I)")
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


