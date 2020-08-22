from datetime import date
ano = int(input("Que ano você nasceu?"))
if ano > date.today().year:
    print ("Você ainda não nasceu!")
else:
    idade= (date.today().year)-ano
    if idade >= 18:
        print ("Você é maior de idade")
    else:
        print ("Ainda faltam \033[1m{}\033[m anos para você ser maior de idade.".format(18-idade))
