import csv
def solucion_es_valida(conjuntos, solucion):
    sets_alcanzados = 0
    for conjunto in conjuntos:
        if conjunto.intersection(solucion):
            sets_alcanzados += 1

    return sets_alcanzados == len(conjuntos)


def _backtrack(conjuntos, conjunto_universo, solucion_actual, solucion, idx):
    if len(solucion_actual) >= len(solucion):
        return
    if idx == len(conjunto_universo):
        if solucion_es_valida(conjuntos, solucion_actual):
            if len(solucion_actual) < len(solucion):
                solucion.clear()
                solucion.extend(solucion_actual)
        return

    solucion_actual.append(conjunto_universo[idx])
    _backtrack(conjuntos, conjunto_universo, solucion_actual, solucion, idx + 1)
    solucion_actual.pop()
    _backtrack(conjuntos, conjunto_universo, solucion_actual, solucion, idx + 1)


def hitting_set(S, U):
    print('hitting set normal ')
    solucion = list(U)
    solucion_actual = []
    _backtrack(S, list(U), solucion_actual, solucion, 0)
    return len(solucion)
