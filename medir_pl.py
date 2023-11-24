
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
        size = hitting_set(conjuntos)
    else:
        size = hitting_set_bilardo(conjuntos)
    return size

# Create and run the algorithm on each test file, measuring run time
files = [5, 7, 10, 15,20, 25, 30,35, 40,45, 50, 60,75,80,90, 100]
run_times = []
sizes_normales = []
sizes_aproximados = []
mayores = []
for i in range(0, len(files)):
    file_name = f"set{files[i]}.txt"
    size, _ = run_algorithm(f"sets_mediciones_normales/{file_name}")
    size_aproximado, mayor = run_algorithm(f"sets_mediciones_normales/{file_name}", True)
    # print(f"Archivo número {files[i]}: {run_time}")
    sizes_normales.append(size)
    sizes_aproximados.append(size_aproximado)
    mayores.append(mayor)

with open("mediciones_comparativas_pl.csv", mode="w") as file:
    file.write("Tamaño de archivo, medicion progamacion lineal normal, medicion programacion aproximada, Mayor elemento, r(I)")
    file.write('\n')
    for i in range(0, len(files)):
        file.write(str(files[i]))
        file.write(',')
        file.write(str(sizes_normales[i]))
        file.write(',')
        file.write(str(sizes_aproximados[i]))
        file.write(',')
        file.write(str(mayores[i]))
        file.write(',')
        file.write(str(sizes_aproximados[i]/sizes_normales[i]))


        file.write('\n')

