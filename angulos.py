import math
angulo = float(input("Digite o angulo "))
seno= math.sin(math.radians(angulo))
cosseno= math.cos(math.radians(angulo))
tangente=math.tan(math.radians(angulo))
print ("O ângulo {}º tem: \n SENO = {:.2f} \n COSSENO ={:.2f} \n 30TANGENTE = {:.2f}" .format(angulo, seno, cosseno, tangente))
