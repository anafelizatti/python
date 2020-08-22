'''print ("-*-"*20)
n1=int(input("Digite um número: "))
print ("-*-"*20)
n2=int(input("Digite outro número: "))
print ("-*-"*20)
n3=int(input("Digite outro número: "))
print ("-*-"*20)
if n1 < n2 and n1 < n3 :
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
else:
    menor = n3
if n1 > n2 and n1 > n3 :
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3
print('Dentre os valores {}, {} e {}, o menor é {} e o maior é {}'.format(n1,n2,n3,menor,maior))'''

primeiro = int(input('Digite o primeiro número:'))
segundo = int(input('Digite o segundo número:'))
terceiro = int(input('Digite o terceiro número:'))
numeros = [primeiro, segundo, terceiro]
print (numeros)
print('O maior valor digitado foi {}'.format(max(numeros)))
print('O menor numero digitado foi {}'.format(min(numeros)))

