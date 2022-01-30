#4) Escribí un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética:
cantidad=0
sumar=0
valor=input("Cuantos numeros desea introducir: ")
while int(valor)> cantidad or cantidad==0: 
    
    valor1=input("Ingrese un numero por favor:  "  )
    print(valor1)
    sumar=sumar+(int(valor1))
    cantidad=cantidad+1

print(float(sumar)/float(cantidad))