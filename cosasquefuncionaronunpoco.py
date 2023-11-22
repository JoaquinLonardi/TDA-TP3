

def solucion_es_valida(conjunto_final, conjuntos_prensa):
    for conjunto_prensa in conjuntos_prensa:
        incluye_jugador = False
        for jugador in conjunto_final:
            if jugador in conjunto_prensa:
                incluye_jugador = True
                continue
        if not incluye_jugador:
            print(f"No es válida: {conjunto_final}")
            return False
    print(f"Es válida: {conjunto_final} --- {len(conjunto_final)}")
    return True


def _algoritmo_backtracking(conjuntos_prensa, conjunto_final, solucion, idx):
    print(solucion)
    if idx < 0:
        print(f"entré por línea 32")
        return solucion_es_valida(solucion, conjuntos_prensa)

    if not solucion_es_valida(solucion, conjuntos_prensa):
        return False

    solucion.remove(solucion[idx])
    if _algoritmo_backtracking(conjuntos_prensa, conjunto_final, solucion, idx - 1):
        return True

    solucion.append(conjunto_final[idx])
    print(f"entré por línea 43")
    return _algoritmo_backtracking(conjuntos_prensa, conjunto_final, solucion, idx - 1)


def algoritmo_backtracking1(conjuntos_prensa):
    conjunto_total = []
    for conjunto in conjuntos_prensa:
        for jugador in conjunto:
            if jugador not in conjunto_total:
                conjunto_total.append(jugador)

    solucion = conjunto_total.copy()

    _algoritmo_backtracking(conjuntos_prensa, conjunto_total, solucion, len(conjunto_total) - 1)
    return len(solucion)



def _algoritmo_backtracking(conjuntos_prensa, conjunto_total, solucion, idx):
    print(solucion)
    if idx >= len(conjunto_total):
        # return solucion_es_valida(solucion, conjuntos_prensa)
        return []

    if solucion_es_valida(solucion, conjuntos_prensa):
        return solucion

    solucion.append(conjunto_total[idx])
    sol_a = _algoritmo_backtracking(conjuntos_prensa, conjunto_total, solucion,  idx + 1)
    if not sol_a:
        solucion.remove(conjunto_total[idx])
        sol_b = _algoritmo_backtracking(conjuntos_prensa, conjunto_total, solucion, idx + 1)
        if sol_b:
            solucion = sol_b if len(sol_b) < len(solucion) else solucion
    else:
        solucion = sol_a if len(sol_a) < len(solucion) else solucion



def algoritmo_backtracking(conjuntos_prensa):
    conjunto_total = []
    for conjunto in conjuntos_prensa:
        for jugador in conjunto:
            if jugador not in conjunto_total:
                conjunto_total.append(jugador)


    solucion = []
    solucion_final = []
    _algoritmo_backtracking(conjuntos_prensa, conjunto_total, solucion, 0)
    return len(solucion)




def _algoritmo_backtracking(conjuntos_prensa, solucion, idx, size):
    print(solucion)
    if solucion_es_valida(solucion, conjuntos_prensa):
        return True
    if idx >= len(conjuntos_prensa):
        return False
    for jugador in conjuntos_prensa[idx]:
        if jugador not in solucion:
            solucion.append(jugador)

        if solucion_es_valida(solucion, conjuntos_prensa):
            return True

        if len(solucion) == size:
            solucion.remove(jugador)

    if not _algoritmo_backtracking(conjuntos_prensa, solucion, idx + 1, size):

        _algoritmo_backtracking(conjuntos_prensa, solucion, 0, size + 1)
    else:
        return True



def _algoritmo_backtracking(conjuntos_prensa, solucion, idx, size, conjunto_total, solucion_final):
    # print(solucion)
    if idx >= len(conjunto_total):
        root = conjunto_total.index(solucion[-size])
        root = root + 1
        if root + 1 > len(conjunto_total):
            size = size + 1
            root = 0

        root = conjunto_total[root]

        solucion = []
        solucion.append(root)

        solucion = _algoritmo_backtracking(conjuntos_prensa, solucion, 0, size, conjunto_total, solucion_final)
        return solucion
    if len(solucion) == size:
        if solucion_es_valida(solucion, conjuntos_prensa):
            return solucion
        else:
            return []

    solucion.append(conjunto_total[idx])

    sol = _algoritmo_backtracking(conjuntos_prensa, solucion, idx + 1, size, conjunto_total, solucion_final)
    if sol:
        return sol

    solucion.remove(conjunto_total[idx])

    return _algoritmo_backtracking(conjuntos_prensa, solucion, idx + 1, size, conjunto_total, solucion_final)