from time import sleep
print ("FOGOS DE ARTIFÍCIO")
for n in range (10,-1,-1):
    print (n)
    if n==10:
         print ("COMEÇANDO!")
    elif n==5:
        print ("QUASE!!")
    elif n==1:
        print ("PREPARE-SE")
    print ('...'*20)
    sleep(1)
print ("FELIZ ANO NOVO!")
