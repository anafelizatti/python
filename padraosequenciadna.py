sequence = str(input(' Digite a sequência: '))
pattern = str(input(' Digite o padrão - sequência a ser encontrada '))
conta = sequence.count(pattern)
print ('A sequência {} \n contém {} repetições do padrão'.format(sequence, conta, pattern))