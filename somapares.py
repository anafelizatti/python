somapares = 0
for i in range (1,51):
    if i % 2 == 0:
        print (i, end=' ')
        somapares += i
print ('\nA soma dos pares é {}'.format(somapares))

#ou for in range (2,50,2) -> començando por 2 até 50, pulando de 2 em 2...