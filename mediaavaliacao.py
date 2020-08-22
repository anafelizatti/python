print ("\033[1;32;40m*****MÉDIA*****\033[m")
nota=float(input("Olá. Digite qual foi sua média \n"))
if 0 < nota < 5:
    print ("Você foi reprovado.")
elif 5.0 <= nota <= 6.9:
    print ('Você está de recuperação.')
elif 7.0 <= nota <= 10 :
    print ("Você foi aprovado.")
else:
    print ("Este não é um valor válido.")

'''if 0 < med < 5.0:
    print('Reprovado , media de {} precisa estudar mais'.format(med))
elif 5.0 <= med <= 6.9:
    print('Está de recuperação , media de {} precisa estudar mais'.format(med))
elif 7.0 <= med <= 10:
    print('Sua nota é {}, Parabéns Aprovado !'.format(med))
else:
    print('Nota inválida')'''

