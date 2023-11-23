import pulp

def solucion_es_valida(conjuntos, solucion):
    sets_alcanzados = 0
    for conjunto in conjuntos:
        if conjunto.intersection(solucion):
            sets_alcanzados += 1

    return sets_alcanzados == len(conjuntos)

def hitting_set(S, U=None):
    if not U:
        U = set()
        for conjunto in S:
            U.update(conjunto)

    variables_elementos = pulp.LpVariable.dicts("elemento", U, cat=pulp.LpBinary)

    hitting_set = pulp.LpProblem("Hitting Set Problem", pulp.LpMinimize)
    hitting_set += pulp.lpSum(variables_elementos)

    for conjunto in S:
        # La suma de las variables -que van a ser 1 o 0- para cada conjunto debe ser mayor a 1. Es decir, debe tener
        # al menos un elemento
        hitting_set += pulp.lpSum(
            variables_elementos[elemento] for elemento in conjunto
        ) >= 1

    hitting_set.solve()

    solucion = {elemento for elemento in hitting_set.variables() if
                elemento.value() == 1
                }

    return len(solucion)
