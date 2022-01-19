from utils import convertListToStr, powerset

def regraContemLambda(rule, regrasLambda):
    for symbol in rule[1]:
        if symbol not in regrasLambda:
            return False
    return True


def regraPossuiSimboloComLambda(rule, regrasLambda):
    for symbol in rule[1]:
        if symbol in regrasLambda:
            return True
    return False


def substituirLambda(rule, power, regrasLambda):
    #print("__________________________________________")
    auxPowerRule=[]
    for i in power:
        auxRule = list(rule)
        #print (f"{i} ------------------")
        for number in i:            
            #print(number)
            if auxRule[number] in regrasLambda:
                #print(auxRule)                    
                auxRule[number] = ""    
                #print(auxRule)               
        auxRule = convertListToStr(auxRule)                  
        if auxRule not in auxPowerRule:                    
            auxPowerRule.append(auxRule)
            #print(auxPowerRule)               
    #print(f"{auxPowerRule}")
    return auxPowerRule


def removerRegrasLambda(variables, terminals, rules, starter): 
    # Encontrando regras lambda (ex: B -> #)
    lambda_1 = set()
    for rule in rules:
        if rule[1] == "#":
            lambda_1.add(rule[0])
    #print(f"regras com lambda = {lambda_1}")

    # Encontrar regras que possuem a regra lambda (ex: A -> BB)
    lambda_2 = lambda_1.copy()
    while True:
        oldLenLambda = len(lambda_2)
        for rule in rules:
            if regraContemLambda(rule, lambda_2):
                lambda_2.add(rule[0])
        if not (len(lambda_2) > oldLenLambda):
            break
    #print(f"regras que possuem lambda = {lambda_2}")  
    
    # Adicionando regras modificadas
    newRules = []
    for rule in rules:
        if regraPossuiSimboloComLambda(rule, lambda_2):
            power = list( powerset( range(0, len(rule[1])) ))
            auxRule = substituirLambda(rule[1], power, lambda_2)
            if len(auxRule) > 1:
                for i in auxRule:
                    tupla = [rule[0], i]
                    if tupla not in newRules:
                        if tupla[0] == starter and tupla[1] == '':
                            tupla[1] = "#"
                        newRules.append(tupla)
            else:
                newRules.append([rule[0],auxRule])
        else:
            if rule[1] == "#" and rule[0] != starter:
                auxRule = ''
                tupla = [rule[0], auxRule] 
                if tupla not in newRules:
                    newRules.append(tupla)
            else:
                if rule not in newRules:
                    newRules.append(rule)

    # Removendo lambda em locais errados e regras desnecessarias (ex: C -> C)
    i=0
    while i < len(newRules):        
        if newRules[i][1] == '' and newRules[i][0] != starter and newRules[i][0] not in lambda_1:
            newRules.pop(i)
            i=0            
        elif newRules[i][0] == newRules[i][1]:
            newRules.pop(i)
            i=0
        else:
            i=i+1

    return newRules


    

