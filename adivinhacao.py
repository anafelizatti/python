from random import randint #da biblioteca RANDOM importar a função de inteiro random
from time import sleep
nropc=(randint(0,5))
print("--" * 20)
nro1=int(input("Digite um número entre  0 e 5: "))
print("--" * 20)
if nro1 >5:
    print ("Não é um número válido!")
else:
    print ("Processando...")
    sleep(1)
    if nro1 == nropc:
        print ("Você adivinhou!")
    else:
        print ("Você errou, o número era {}".format(nropc))

