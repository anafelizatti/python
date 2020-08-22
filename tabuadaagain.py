n = int(input("Qual tabuada você quer ver?"))
if n > 10 or n < 0:
    print("Número inválido!")
else:
    print("A tabuada do {} é:".format(n))
    for i in range(0, 11):
        resultado = n * i
        print('{} X {} = {}'.format(n, i, resultado))
