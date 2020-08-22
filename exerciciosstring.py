nome=str(input("Qual seu nome? ")).strip() #strip elimina espaços
print ("Seu nome em Maiúsculas é {}\nSeu nome em minúsculas é {}". format (nome.upper(), nome.lower()))
print ("Seu nome completo tem {} letras".format(len(nome)-(nome.count(" "))))
#print ("Seu primeiro nome tem {} letras" .format(nome.find(" "))) #vai encontrar onde está o primeiro espaço, e indicar o nro do caracter até chegar a ele, que contém o primeiro nome.
separa = nome.split() #vai separar onde tiver espaços, formando blocos (bloco 0, 1, 2, 3...a cada espaço)
print ("Seu primeiro nome é {} e tem {} letras ".format (separa[2].capitalize(),len(separa[2])))