import math #importar biblioteca matemática do python
#ou from math import trunc -> para importar somente a função de interesse : nesse caso, não precisa colocar math.trunc,
#apenas citar o trunc -> .format(trunc(var))
valor = float(input("Digite o valor: "))
print("O valor {} tem sua parte inteira {}".format(valor, math.trunc(valor)))
print ("O valor {} é a porção inteira".format(int(valor))) #função int também faz a mesma coisa
#portanto pode usar biblioteca de funções, importar só uma função ou usar "int"
