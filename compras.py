price=(float(input("Qual o valor das suas compras? \nR$")))
nro=(int(input("Escolha a forma de pagamento: \n [1] À VISTA - DINHEIRO \n [2] DÉBITO \n [3] 2x \n [4] Mais parcelas \n")))
if nro ==1:
    print ("Seu pagamento é em dinheiro a vista. Total R${:.2f}".format(price))
    print ("Você terá um desconto de 10% e pagará R${:.2f}".format(price-((price*10)/100)))
elif nro==2:
    print("Seu pagamento é pelo cartão de débito. Total R${:.2f}".format(price))
    print("Você terá um desconto de 5% e pagará R${:.2f}".format(price - ((price * 5) / 100)))
elif nro==3:
    print("Seu pagamento é no cartão de crédito. Total R${:.2f}".format(price))
    print("Você pagará 2 parcelas de R${:.2f}.".format(price/2))
elif nro ==4:
    parcelas=int(input('Quantas parcelas?'))
    juros= (price*20)/100
    precoparcelas=(price+juros)/parcelas
    print("Seu pagamento será em {} vezes. Total inicial R${:.2f}".format(parcelas,price))
    print("Você terá juros de 20% e pagará um total de R${:.2f} em {} parcelas de R${:.2f}".format(price + juros, parcelas, precoparcelas))
else:
    print ("Opção inválida")


