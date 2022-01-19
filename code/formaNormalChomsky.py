from utils import convertListToStr

ALFABETO = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def novaVariavel(variables):
    for letter in ALFABETO:
        if letter not in variables:
            return letter
    print("NAO HA LETRA DO ALFABETO DISPONIVEL")
    return None


def regraRepresentada(symbol, rules, newVariables):
    for rule in rules:
        if rule[1] == symbol and rule[0] in newVariables:
            return True, rule[0]
    return False, None


def substituirSimbolo(newRule, oldValue, newValue):
    auxRule = list(newRule)
    for id, item in enumerate(auxRule):
        if item == oldValue:
            auxRule[id] = newValue
    return convertListToStr(auxRule)


def substituirVariaveis(newRule, oldValue, newValue):
    if newRule.find(newValue):
        newRule = newRule.replace(oldValue, newValue)
        return newRule


def modificarRegra(variables, terminals, rules, starter):
    newVariables = variables.copy()
    newRules = []
    
    auxNewRule = False
    newRule = None
    newVar = None

    for rule in rules:
        if len(rule[1]) >= 2:
            auxNewRule = False
            newRule = rule[1]
            for symbol in rule[1]:
                if symbol in terminals:
                    auxNewRule = True
                    auxNewVar, var = regraRepresentada(symbol, newRules, newVariables)                    
                    if not auxNewVar:                    
                        newVar = novaVariavel(newVariables)
                        newVariables.append(newVar)
                        newRules.append([newVar, symbol])
                        newRule = substituirSimbolo(newRule, symbol, newVar)                                               
                    else:
                        newRule = substituirSimbolo(newRule, symbol, var)
            if auxNewRule:
                newRule =  [rule[0], newRule]
                newRules.append(newRule)
            else:
                newRules.append(rule)
        else:
            newRules.append(rule)

    return newRules, newVariables


def substituirRegra(variables, terminals, rules, starter):
    newVariables = variables.copy()
    newRules = rules.copy()
    rulesToRemove = []

    auxNewRule = ''
    newRule = None
    newVar = None

    for rule in rules:
        if len(rule[1]) >= 3:
            auxNewRule = ''
            newRule = list(rule[1])
            for i in range(1, len(newRule)):
                auxNewRule = auxNewRule + newRule[i]
            auxNewVar, var = regraRepresentada(auxNewRule, newRules, newVariables)    
            newRule = convertListToStr(newRule)
            if not auxNewVar:                    
                newVar = novaVariavel(newVariables)                
                newVariables.append(newVar)
                newRules.append([newVar, auxNewRule])
                newRule = substituirVariaveis(newRule, auxNewRule, newVar)                
            else:
                newRule = substituirVariaveis(newRule, auxNewRule, var)
            newRules.append([rule[0], newRule])               
        else:
            newRules.append(rule)            
        rulesToRemove.append(rule) 
        
    for rule in rulesToRemove:
        newRules.remove(rule)

    return newRules, newVariables

