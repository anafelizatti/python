import math
# or from math import hypot **
cop = float (input("Digite o cateto oposto: "))
cad = float (input("Digite o cateto adjacete: "))
hipotenusa = math.hypot(cop,cad)
#hipotenusa = hypot(cop,cad)**
#hipotenusa = (((cop ** 2) + (cad **2)) ** 0.5)***
print ("A hipotenusa é {:.2f} ".format(hipotenusa))