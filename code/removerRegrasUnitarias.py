def gerarEncadeamento(var, variables, rules, closure):
    for rule in rules:
        if var is rule[0]:
            if len(rule[1]) == 1 and rule[1][0] in variables:
                closure.append(rule[1][0])


def buscarRegrasNaoUnicasPorVariavel(rules, variables, var):
    newRules = []
    for rule in rules:
        if rule[0] == var:
            if len(rule[1]) == 1:
                if rule[1][0] not in variables:
                    newRules.append(rule)
            else:
                newRules.append(rule)
    return newRules


def substituirRegrasUnitarias(rules, variables, newRules, closure, var, ):
    for rule in rules:
        if rule[0] == var:
            if len(rule[1]) == 1:
                if rule[1][0] not in variables:
                    newRules.append([closure, rule[1]])
            else:
                newRules.append([closure, rule[1]])


def removerRegrasUnitarias (variables, terminals, rules, starter):
    closures = {}

    # Gerando encadeamentos (ex: enc(P))
    for var in variables:
        closures[var] = [var]
        gerarEncadeamento(var, variables, rules, closures[var])
    
    # Novas regras
    newRules = []
    auxNewRules = []
    for closure in closures.keys():
        auxNewRules = buscarRegrasNaoUnicasPorVariavel(rules, variables, closure)
        for var in closures[closure]:
            if var != closure:
                substituirRegrasUnitarias(rules, variables, auxNewRules, closure, var)
        for auxRule in auxNewRules:
            if auxRule not in newRules:
                newRules.append(auxRule)
    
    return newRules