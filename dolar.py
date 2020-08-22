#dolar = float(input("Quantos reais você tem? "))
#print ("Você pode comprar {} dólares".format(dolar/4.8))

#largura= float(input("Qual a largura da sua parede?"))
#altura = float(input("Qual a altura da sua parede?"))
#area = largura*altura
#tinta = area*2
#print ("Você precisará de {} litros de tinta para pintar {} m²".format(tinta, area))

price=float(input('Qual o valor do produto? '))
salary=float(input('Qual seu salário? '))
desconto=(price-((price*5)/100))
adicional=(salary+(salary*15/100))
print ("O valor do produto é {} e com desconto de 5% é {}". format(price,desconto))
print ("Seu salário de {} com adicional de 15% é {}". format (salary,adicional))