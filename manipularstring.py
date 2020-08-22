sequence = input ("DIGITE A FRASE")
print(sequence[0:5])#[9:20] -> do 10º ao 19ºnro
print(sequence[0:4:3])#do n1 ao n2, pulando de n3 em n3
print(sequence[:5])#vai do zero até o n, nesse caso até o quarto; ou [15:] -> exibe a partir do 15 até o final
print(sequence[n::3]) #mostra do n até o final, mas pulando de 3 em 3
print(len(sequence))#tamanho de caracteres
print(sequence.count("A",0,4)) #contar quantos A tem começando pelo caractere de nro 0 até o caractere de nro 3. (4-1)
print(sequence.find("G")) #ENCONTRAR EM QUE posição COMEÇA A SEQUÊNCIA PROCURADA
print ("teste" in sequence) #vai aparecer true ou false se tiver aquilo ou não
print(sequence.replace("A", "G"))
print (sequence.upper()) #colocar maiusculo
print (sequence.lower())#minisculo
sequence.capitalize() #só mantém o primeiro caractere em maiusculo
sequence.title() #coloca as primeiras letras de cada palavra em maiusculo
sequence.strip() #tira os espaços do começo e final; poder ser lstrip ou rstrip para tirar da esquerda ou direita
#textolongo = aspas triplas """
