# from math import factorial
# n=int(input("Digite um número"))
# print (factorial(n))

n = int(input("Digite o número: \n ->"))
c = n
f = 1
print ("Calculando o fatorial de {}! ".format(n))
while c > 0:
    print (('{}'.format(c)), end='')
    print ((' x ') if c > 1 else ' = ' ,end='')
    f = f*c
    #1 = 1*5
    #5=5*4
    #20=20*3
    #60=60*2
    #120=120*1
    c = c - 1
print (f)

