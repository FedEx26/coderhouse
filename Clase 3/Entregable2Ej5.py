#5) Escribí un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. 
# Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:
# La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False)
Lista_numeros=[1,3,6,9]
valor=input("Ingrese un numero entero entre 0 y 9 por favor:  "  )

while int(valor)<= 0 or int(valor)>9:  
    valor=input("Ingrese un numero entero entre 0 y 9 por favor:  "  )
    print(valor)
print(valor)

x = Lista_numeros.__contains__(int(valor))
if (x==True):
    print("El numero esta presente en la lista")
else:
    print("El numero no esta en la lista")