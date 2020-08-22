'''salary=float(input("Salário: "))
if salary >1250.00 :
    print ("O salário de R${:.2f} terá um aumento de 10%, totalizando R${:.2f}".format ((salary),((salary)+(salary*10)/100)))
else:
    print ('O salário de R${:.2f} terá um aumento de 15%, totalizando R${:.2f}'.format ((salary),((salary)+(salary*15)/100)))'''
produto = float(input("Olá, qual valor do produto?"))
if produto <= 100:
    desconto = ((produto*10)/100)
    print ("\033[1;31;43mSeu desconto será de 10%.O valor do desconto será R${:.2f}, totalizando R${:.2f}\033[m".format(desconto,(produto-desconto)))
else:
    desconto = ((produto * 15) / 100)
    print("\033[1;37;45mSeu desconto será de 15%. O valor do desconto será R${:.2f}, totalizando R${:.2f}\033[m".format(desconto, (produto - desconto)))

