from random import randint
from time import sleep
n1=int(input("ESCOLHA: \n [1] PEDRA \n [2] PAPEL \n [3] TESOURA \n->"))
if n1==1:
    escolha="PEDRA"
elif n1==2:
    escolha="PAPEL"
elif n1==3:
    escolha="TESOURA"
elif n1 >3 or n1 <1:
    print ("Inválido!")
nropc=randint(1,3)
if nropc==1:
    pc="PEDRA"
elif nropc==2:
    pc="PAPEL"
elif nropc==3:
    pc="TESOURA"
sleep((1))
print("JO...")
sleep((1))
print("KEN...")
sleep((1))
print("PO...")
print('***'*20)
print ("Você escolheu {} e o PC escolheu {}".format(escolha,pc))
print('***'*20)
if n1 == nropc:
    print(escolha,"VS",pc)
    print('***' * 20)
    (sleep(1))
    print ("\033[1;34;41mEMPATE!\033[m")
elif (n1 == 1 and nropc ==3) or (n1==3 and nropc==2) or (n1==2 and nropc==1):
    print(escolha, "VS", pc)
    print('***' * 20)
    (sleep(1))
    print ("\033[1;34;41mVocê venceu!\033[m\n{} VS {}, {} vence".format(escolha,pc,escolha))
else:
    print(escolha, "VS", pc)
    print('***' * 20)
    (sleep(1))
    print ("\033[1;34;41mVocê perdeu!\033[m\n{} VS {}, {} vence".format(escolha,pc,pc))


#from random import randint
#itens = ("Pedra", "Papel", "Tesoura")
#computador = randint(0,2)
#print ('''Escolha:
#[0] PEDRA
#[1] PAPEL
#[2] TESOURA''')
#jogador=int(input('Qual a sua jogada?'))
#print ("O PC escolheu {}".format(itens[computador])) #escolher itens de uma lista ordenada; 0=pedra,1=papel...
#print ("O Jogador escolheu {}".format(itens[jogador]))'''