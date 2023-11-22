def solucion_es_valida(conjuntos, solucion):
    sets_alcanzados = set()
    sets_alcanzados = 0
    for conjunto in conjuntos:
        if conjunto.intersection(solucion):
            sets_alcanzados += 1

    return sets_alcanzados == len(conjuntos)
def _backtrack(conjuntos, conjunto_universo, solucion_actual, solucion, idx):

    if len(solucion_actual) >= len(solucion):
        print(f"No vale la pena chequear: {solucion_actual}")
        return
    print(f"chequeo {solucion_actual}")
    if idx == len(conjunto_universo):
        if solucion_es_valida(conjuntos, solucion_actual):
            if len(solucion_actual) < len(solucion):
                solucion.clear()
                solucion.extend(solucion_actual)
                print(f"encontre una mejor solucion. {solucion}")
        return

    solucion_actual.append(conjunto_universo[idx])
    _backtrack(conjuntos, conjunto_universo, solucion_actual, solucion, idx + 1)
    solucion_actual.pop()
    _backtrack(conjuntos, conjunto_universo, solucion_actual, solucion, idx + 1)

def hitting_set(conjuntos):
    conjunto_universo = set()
    for conjunto in conjuntos:
        conjunto_universo.update(conjunto)

    solucion = list(conjunto_universo)
    solucion_actual = []
    _backtrack(conjuntos, list(conjunto_universo), solucion_actual, solucion, 0)
    print(solucion)
    return len(solucion)