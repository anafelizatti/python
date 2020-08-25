from random import randint
ganhador = (' ')
tentativas = 0
empate=0
invalido = 0
print ("Olá! Sou seu computador e pensei em um número de 1-10! Tente adivinhar um número maior!")
while ganhador != 'VOCÊ' or ganhador == "INVÁLIDO":
    player1 = int(input("Digite um número de 1 a 10:-> "))
    playerpc = randint(1, 10)
    if player1 > 10:
        ganhador='INVÁLIDO'
        print ("INVÁLIDO!")
        invalido += 1
    elif player1 < playerpc:
        ganhador = ("PC")
        print (ganhador)
        print ("Você errou!")
        print ("PC {} > {} VOCÊ ".format(playerpc,player1))
        tentativas += 1
    elif player1 > playerpc:
        ganhador = ('VOCÊ')
        print (ganhador)
        print ("Você venceu!")
        print ("VOCÊ {} > {} PC".format(player1,playerpc))
    elif player1 == playerpc:
        ganhador = ('EMPATE!')
        print (ganhador)
        print("VOCÊ {} = {} PC".format(player1, playerpc))
        empate =+1
print ("FIM")
print ("Você perdeu {} vezes e empatou {} vezes até vencer.\nTentativas inválidas : {} ".format(tentativas,empate,invalido))


