maistermos=' '
totaltermos = 0
nroi=0
nro = int(input("Digite o número\n ->"))
nroi=nro
razao = int(input("Digite a razão\n ->"))
termos = int(input("Quantos termos você quer ver?\n ->"))
totaltermos += termos
print(nroi,end=' ')
for c in range(1, termos+1):
    nro += razao
    print(nro,end=' ')
while maistermos != "N":
    maistermos = input("\nVocê quer mais termos? [S] ou [N]?").upper().strip()
    if maistermos =='S':
        termos2=int(input("Quantos termos?"))
        totaltermos += termos2
    for c in range (1, termos2+1):
        nro += razao
        print(nro, end=' ')
    if maistermos=='N':
        print ("FIM!")
print ("Você fez a PA iniciando em {}, com razão de {} e {} termos".format(nroi,razao,totaltermos))
