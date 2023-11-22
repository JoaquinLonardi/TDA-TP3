import csv


def leer_archivo(filename):
    import os
    path = os.path.join("../archivos_prueba", filename)
    conjuntos_periodistas = []
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for x in reader:
            conjuntos_periodistas.append(set(x))

    return conjuntos_periodistas


def solucion_es_valida(conjunto_final, conjuntos_prensa):
    for conjunto_prensa in conjuntos_prensa:
        if not conjunto_final.intersection(conjunto_prensa):
            return False
    return True

def hits(conjunto_final, conjuntos_prensa):
    hits = 0
    for conjunto_prensa in conjuntos_prensa:
        incluye_jugador = False
        for jugador in conjunto_final:
            if jugador in conjunto_prensa:
                hits = hits + 1
                incluye_jugador = True
                break
    return hits

def combinations(lst, k):
    if k == 0:
        return [[]]

    if not lst:
        return []

    head, tail = lst[0], lst[1:]
    with_head = [[head] + rest for rest in combinations(tail, k - 1)]
    without_head = combinations(tail, k)

    return with_head + without_head

def set_combinations(s, k):
    if k == 0:
        return [set()]

    if not s:
        return []

    head, *tail = s
    with_head = [set({head}).union(rest) for rest in set_combinations(tail, k - 1)]
    without_head = set_combinations(tail, k)

    return with_head + without_head


def _algoritmo_backtracking(conjuntos_prensa, solucion, idx, size, conjunto_total, solucion_final):

   for c in combinations(conjunto_total, size):
       # hits = hits(c, conjuntos_prensa)

       if solucion_es_valida(c, conjuntos_prensa):
           return c
   return None

def algoritmo_backtracking(conjuntos_prensa):
    conjunto_total = set()
    for conjunto in conjuntos_prensa:
        for jugador in conjunto:
            if jugador not in conjunto_total:
                conjunto_total.add(jugador)

    solucion = []
    solucion_final = []
    # for i in range(1, 1000000):
    #     solution = _algoritmo_backtracking(conjuntos_prensa, solucion, 0, i, conjunto_total, solucion_final)
    #     if solution:
    #         return len(solution)
    # asd = MTMiner(conjuntos_prensa)
    # asd = find_minimum_hitting_set(conjunto_total, conjuntos_prensa)
    print(f"solucion es: {solucion}")
    print(f"solucion final es: {solucion_final}")
    # print(f"return value es: {asd}")
    # return len(solucion)
    from vertex_cover import hitting_set
    asd = hitting_set(conjuntos_prensa)
    return asd

def hits_fewer_sets(menor, mayor, conjuntos_prensa):
    hits_menor = 0
    conjuntos_prensa_copy = conjuntos_prensa.copy()
    conjuntos_prensa_copy2 = conjuntos_prensa.copy()
    for jugador in menor:
        for conjunto in conjuntos_prensa_copy2:
            if jugador in conjunto:
                hits_menor = hits_menor + 1
                conjuntos_prensa_copy2.remove(conjunto)
                continue
    hits_mayor = 0
    for jugador in mayor:
        for conjunto in conjuntos_prensa_copy:
            if jugador in conjunto:
                hits_mayor = hits_mayor + 1
                conjuntos_prensa_copy.remove(conjunto)
                continue

    return hits_menor < hits_mayor


    return hits

def MTMiner(conjuntos_prensa):
    conjunto_total = set()
    for conjunto in conjuntos_prensa:
        for jugador in conjunto:
            if jugador not in conjunto_total:
                conjunto_total.add(jugador)

    Cs = [0] * 40
    Cs[1] = conjunto_total
    i = 1
    while Cs[i]:
        Cs[i+1] = set()
        for ab in set_combinations(Cs[i], i+1):
            c = ab
            for e in c:
                c2 = c.copy()
                c2.remove(e)
                if hits_fewer_sets(c2, c, conjuntos_prensa):
                    # print(c)
                    if solucion_es_valida(c, conjuntos_prensa):
                        # print(c)
                        return c
                    else:
                        Cs[i+1].add(e)
                # else:
                    # print(f"Creo que este no lo tengo en cuenta: {c}")

        i += 1