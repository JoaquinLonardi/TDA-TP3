import sys
from algoritmo import hitting_set
from programacion_lineal import hitting_set_pl
from programacion_lineal import hitting_set_aprox
import csv

def leer_archivo(filepath):
    conjuntos_periodistas = []
    with open(filepath, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for x in reader:
            conjuntos_periodistas.append(set(x))

    conjunto_universo = set()
    for conjunto in conjuntos_periodistas:
        conjunto_universo.update(conjunto)

    return conjuntos_periodistas, conjunto_universo


if len(sys.argv) == 1:
    print('ERROR: Falta especificar el archivo como argumento.')
    sys.exit()


if len(sys.argv) == 2:
    print(f"ERROR: Falta especificar el flag de función")
    sys.exit()

S, U = leer_archivo(sys.argv[1])
flag = sys.argv[2]

if flag == '-bt':
    solucion = hitting_set(S, U)
elif flag == '-pl':
    solucion = hitting_set_pl(S, U)
elif flag == '-aprox':
    solucion = hitting_set_aprox(S, U)
else:
    print(f"ERROR: Flag incorrecto. Las opciones posibles son {['-bt', '-pl', '-aprox']}")
    sys.exit()

print(f"La mínima cantidad de jugadores que puede llevar Scaloni para contentar al periodismo es: {solucion}")