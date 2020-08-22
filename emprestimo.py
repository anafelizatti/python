houseValue=(float(input('Qual o valor do imóvel \n')))
salary=(float(input('Qual seu salário? \n ')))
paymentYears=int(input('Em quantos anos você quer pagar? \n'))
render=(houseValue/(paymentYears*12))
salarypercent = ((salary*30)/100)
if render > salarypercent:
    print ("Seu salário é de R${:.2f}, e o valor máximo de prestação que você pode pagar é R${:.2f}.\n "
           "O valor calculado de parcela é de R${:.2f} mensal. \n \33[1;41;34m*Empréstimo negado*.\33[m".format(salary,salarypercent,render))
elif render < salarypercent:
    print ("Seu salário é de R${:.2f}, e o valor máximo de prestação que você pode pagar é R${:.2f}.\n "
           "O valor calculado de parcela é de R${:.2f} mensal. \n \33[1;41;34m*Empréstimo aprovado*.\33[m".format(salary,salarypercent,render))
else:
    print ("Valor inválido")
print ("******"*20)