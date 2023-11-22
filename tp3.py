import sys
from algoritmo import algoritmo_backtracking
import csv

def leer_archivo(filename):
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for x in reader:
                print(x)
    except OSError:
        print('ERROR: Archivo no encontrado.')
        sys.exit()


if len(sys.argv) == 1:
    print('ERROR: Falta especificar el archivo como argumento.')
    sys.exit()
