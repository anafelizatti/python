#frase = str(input("Digite sua frase: ")).strip().upper()
#print ('A letra A aparece {} vezes'.format(frase.count("A")))
#print ('A primeira letra A está na posição {}'.format(frase.find("A")+1))
#print ('A  ultima  letra A está na posição {}'.format(frase.rfind("A")+1))

nome = str(input ("Seu nome completo é:")).strip().upper() #remove espaços deixa tudo maiusculo
separa = nome.split() #separa em blocos
space= nome.count(" ") #conta os espaços entre os blocos para definir o nro de blocos
print ("Seu primento nome é {}".format((separa[0].capitalize()))) #pega o primeiro bloco - 0
print ("Seu nome do meio é {}".format(separa[space-1].capitalize())) #PEGA O BLOCO ANTES DO ULTIMO
print ("Seu último nome é {}".format (separa[space].capitalize())) #PEGA O ULTIMO BLOCO

