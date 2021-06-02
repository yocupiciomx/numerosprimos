# -*- coding: utf-8 -*-
# realizado por Angel Yocupicio
# yocupicio.com
# Versión de Python 3.9.x
# Hecho en GNU/Linux, Manjaro Linux

n=int(input("¿Hasta qué número deseas generar los números primos? "))
print("Números primos entre 1 y {}".format(n))

lista=[2,]  
for i in range(3,n,2):  
 	for j in range(3,i,2):  
  		if i%j==0:  
   			break  
 	else:
  		lista.append(i)  
print(lista)

imprimir = str(input("¿Deseas imprimirlos en un archivo .docx? (si,no) "))
if imprimir == "si":
	v = open("primosv2.docx","w")
	v.write("{}\n".format(lista))
	v.close()
	print("Puedes ver tales números primos en el archivo primosv2.docx")

print("FIN")
