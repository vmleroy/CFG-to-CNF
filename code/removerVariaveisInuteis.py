def regraGeraTerminal (rule, terminals, ix):
    for symbol in rule[1]:
        if not (symbol in terminals or symbol in ix):
            return False
    return True


def checarSeVariaveisEstaoEmNx (rule, variables, nx):
    if rule[0] not in nx:
        return False
    
    for symbol in rule[1]:
        if symbol not in nx and symbol in variables:
            return False

    return True


def checarSeTerminaisEstaoEmIx (rule, terminals, ix):
    for symbol in rule[1]:
        if symbol in terminals and symbol not in ix:
            return False
    return True


def removerVariaveisInuteis(variables, terminals, rules, starter):
    
    # Descobrindo regras que geram algum simbolo (ex: 1 ou a)
    n1 = set()
    while True:
        oldLenV1 = len(n1)
        for rule in rules:
            if rule[1] != '' and regraGeraTerminal(rule, terminals, n1):
                n1.add(rule[0])
        if not (len(n1) > oldLenV1):
            break

    # Removendo regras que possuem regras que nao estao presentes em "n1"
    # Em outras palavras, finalizando primeira parte do passo
    regrasPrimeiroPasso = []
    for rule in rules:
        if rule[1] != '' and checarSeVariaveisEstaoEmNx(rule, variables, n1):
            regrasPrimeiroPasso.append(rule)

    # Segundo passo do algoritmo
    i = set()
    n2 = set()
    n2.add(starter)
     
    while True:
        oldLenI = len(i)
        oldLenN = len(n2)
        for rule in regrasPrimeiroPasso:
            if rule[0] in n2:
                for symbol in rule[1]:
                    if symbol in n1:
                        n2.add(symbol)
                    elif symbol in terminals:
                        i.add(symbol)
        if not (len(n2) > oldLenN and len(i) > oldLenI):
            break

    # Finalizando segundo passo
    newRules = []
    for rule in regrasPrimeiroPasso:
        if checarSeVariaveisEstaoEmNx(rule, n1, n2):
            if checarSeTerminaisEstaoEmIx(rule, terminals, i):
                newRules.append(rule)

    return newRules, list(n2)
            

    