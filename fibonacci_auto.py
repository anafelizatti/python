t1= t3 =0
t2=1
cont = 3 #pq t1 e t2 já tem...
n=int(input('Quantos termos de Fibonacci você quer ver?'))
print (t1' ',t2 , end=' ') #FORA DO WHILE PQ VAI MOSTRAR O VALOR FIXO...
while cont <= n:
    t3 = t1+t2
    print (t3, end=' ')
    t1=t2
    t2=t3
    cont += 1
print ('FIM')

#enquanto o contador for menor ou igual ao nro de termos escolhidos
#t3 vai receber a soma dos dois anteriores, t1 e t2
#t1 vai virar t2, e t2 vai virar t3, para que o proximo t3 do laço receba a soma de seus anteriores imediatos
