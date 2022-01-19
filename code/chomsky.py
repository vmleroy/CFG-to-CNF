import json
import jsbeautifier

from formaNormalChomsky import modificarRegra, substituirRegra
from removerRegrasLambda import removerRegrasLambda
from removerRegrasUnitarias import removerRegrasUnitarias
from removerVariaveisInuteis import removerVariaveisInuteis

def createAnswer(rules, variablesStart, variablesEnd, starter):
    #print(variablesStart, variablesEnd)
    varStart = variablesStart.copy()
    varStart.sort()
    varEnd = variablesEnd.copy()
    varEnd.sort()
    varStartD = {}
    varEndD = {}
    for var in varStart:
        if var != starter:
            varStartD[var] = []
    for var in varEnd:
        if var not in variablesStart:
            varEndD[var] = []
    answer = {}
    answer[starter] = []
    answer.update(varStartD)  
    answer.update(varEndD)
    for rule in rules:
        answer[rule[0]].append(rule[1])
    newVar = list(answer.keys())
    return answer, newVar


def saidaJson(variables, terminals, rules, starter):
    auxRules = []
    for var in rules.keys():
        for rule in rules[var]:
            auxRules.append([var, rule])
    data = {}
    data["glc"] = [variables, terminals, auxRules, starter]
    json_data = json.dumps(data)
    options = jsbeautifier.default_options()
    options.indent_size = 2
    print(jsbeautifier.beautify(json_data, options))


def chomsky(variables, terminals, rules, starter):
    #print(f"{variables}\n{terminals}\n{rules}\n{starter}")    
    regrasSemLambda = removerRegrasLambda(variables, terminals, rules, starter)
    #print(f"regras sem lambda:\n{regrasSemLambda}\n")
    regrasNaoUnitarias = removerRegrasUnitarias(variables, terminals, regrasSemLambda, starter)
    #print(f"regras nao unitarias:\n{regrasNaoUnitarias}\n")
    regrasSemVariaveisInuteis, newVariables1 = removerVariaveisInuteis(variables, terminals, regrasNaoUnitarias, starter)
    #print(f"regras sem variaveis inuteis:\n{regrasSemVariaveisInuteis}\n")
    regraModificada, newVariables2 = modificarRegra(newVariables1, terminals, regrasSemVariaveisInuteis, starter)
    #print(f"\nregras modificada:\n{regraModificada}\n")
    regraFinal, newVariables3 = substituirRegra(newVariables2, terminals, regraModificada, starter)
    #print(f"\nregras final:\n{regraFinal}\n")
    answer, finalVariables = createAnswer(regraFinal, newVariables1, newVariables3, starter)
    #print(answer)
    saidaJson(finalVariables, terminals, answer, starter)
