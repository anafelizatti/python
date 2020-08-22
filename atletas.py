from datetime import date
ano = int(input("Informe o \033[1mano\033[m de nascimento: "))
idade = date.today().year - ano
if idade < 0:
    print("Você nem nasceu ainda.")
elif idade <= 9:
    print("Com {} anos você está no grupo MIRIM.".format(idade))
elif idade <= 14:
    print("Com {} anos você está no grupo INFANTIL.".format(idade))
elif idade <= 19:
    print("Com {} anos você está no grupo JÚNIOR.".format(idade))
elif idade <= 25:
    print("Com {} anos você está no grupo SÊNIOR.".format(idade))
else:
    print("Com {} anos você está no grupo MASTER.".format(idade))
