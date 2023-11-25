import pulp


def solucion_es_valida(conjuntos, solucion):
    sets_alcanzados = 0
    for conjunto in conjuntos:
        if conjunto.intersection(solucion):
            sets_alcanzados += 1

    return sets_alcanzados == len(conjuntos)


def hitting_set_pl(S, U):
    variables_elementos = pulp.LpVariable.dicts("elemento", U, cat=pulp.LpBinary)

    hitting_set = pulp.LpProblem("Hitting Set Problem", pulp.LpMinimize)
    hitting_set += pulp.lpSum(variables_elementos)

    for conjunto in S:
        hitting_set += pulp.lpSum(
            variables_elementos[elemento] for elemento in conjunto
        ) >= 1

    hitting_set.solve()
    valores = [elemento.value() for elemento in hitting_set.variables()]
    solucion = {elemento for elemento in hitting_set.variables() if
                elemento.value() == 1
                }

    return len(solucion)


def hitting_set_aprox(S, U):
    variables_elementos = pulp.LpVariable.dicts("elemento", U, lowBound=0, upBound=1)
    hitting_set_problem = pulp.LpProblem("Hitting Set Problem", pulp.LpMinimize)

    # funcion a optimizar
    hitting_set_problem += pulp.lpSum(variables_elementos)

    max_cardinalidad_conjunto = max([len(conjunto) for conjunto in S])

    for conjunto in S:
        hitting_set_problem += pulp.lpSum(
            variables_elementos[elemento] for elemento in conjunto
        ) >= 1

    hitting_set_problem.solve()

    solucion = 0
    for elemento in hitting_set_problem.variables():
        valor = elemento.value()
        if valor >= 1 / max_cardinalidad_conjunto:
            solucion += 1

    return solucion
