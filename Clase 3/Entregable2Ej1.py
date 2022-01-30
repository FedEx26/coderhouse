import sys
num1=int(input("ingrese un numero:  "))
num2=int(input("ingrese otro numero:  "))
op=int(input("Elija el proceso deseado 1-Suma 2-Resta 3-Multiplicacion 4-Finalizar :  " ))
int(op)
while op != 4:
    if op >= 5 or op<1:
        op = int(input("""Ingresa Otra Opcion Valida...Sin letras y numeros entre 1 y 4 """ )) 
        if op == 4:
            print(" Programa finalizado ")
            break
    if op == 1:
            suma=int(num1)+int(num2)
            print(suma)
    elif op == 2:
       resta=int(num1)-int(num2)
       print(resta)
    elif op == 3:
        multi=int(num1)*int(num2)
        print(multi)
    op = int(input("Ingrese su nueva Opcion: "))
else: 
    print(" Programa finalizado ")
