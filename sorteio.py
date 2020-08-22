from random import choice,shuffle
n1=input("Digite um nome: ")
n2=input("Digite um nome: ")
n3=input("Digite um nome: ")
n4=input("Digite um nome: ")
lista = [n1,n2,n3, n4] #quando é lista tem que ser colchetes.
sorteado = choice(lista)
print (sorteado)
shuffle(lista)
print (lista)
