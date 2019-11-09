#INPUT
Comensal=input("ingrese nombre del comensal:")
Azafata=input("ingrese el nombre de la azafata:")
arroz_mariscos=input("ingrese el precio de arroz con mariscos:")
refresco_lima=input("ingrese el precio de refresco de lima :")
ocopa=input("ingrese el precio de ocopa:")

#PROCESSING
arroz_mariscos=(4* ocopa)
ocopa=(refresco_lima+1)
refresco_lima=(arroz_mariscos//5)

#OUTPUT
print("#############################################")
print("# CEVICHERIA - SEÑOR DELFIN ")
print("#############################################")
print("#Comensal: ", Comensal  +  " Azafata: ", Azafata)
print("#Arroz con mariscos: ", arroz_mariscos)
print("#refresco de lima: ", refresco_lima)
print("#ocopa: ", ocopa)
