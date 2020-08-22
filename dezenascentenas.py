nro=int(input("Digite o número: "))
if nro > 9999 :
    print("Não é válido")
else:
#n=str(nro)
#print ("Milhar: {} \n Centena: {} \n Dezena: {} \n Unidade: {} ". format(n[0],n[1],n[2],n[3]))
    u = nro // 1 % 10 # dividir por 1 e depois por 10, pegar o resto. 1000/1 = 1000. 1000/10 = resto 0, unidade =0
    d = nro // 10 % 10
    c = nro // 100 % 10
    m = nro // 1000 % 10
    print ("Milhar: {} \n Centena: {} \n Dezena: {} \n Unidade: {} ". format(m,c,d,u))
