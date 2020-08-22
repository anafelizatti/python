
'''frase = input("Qual a frase? ").upper().replace(" ", "")
reverso = frase[::-1]
if frase == frase[::-1]: #[:inicio,:fim,-1:inverso]
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo")
print ('A frase foi',frase)
print ('O oposto dela é', reverso)'''
frase = ''.join(str(input('Diga uma frase: ')).split()).lower() #separar a frase, deixar em minuscula e juntar tudo sem espaço)
print('A frase digitada foi:\n{}\nE o contrário dela é:\n{}'.format(frase, ''.join(reversed(frase))))
if ''.join(reversed(frase)) == frase:
    print('Portanto, ela é um palíndromo!')
else:
    print('Portanto, ela não é um palíndromo.')
