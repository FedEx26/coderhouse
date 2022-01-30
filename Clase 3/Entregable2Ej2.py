#2) Escribí un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.

num=input("ingrese un numero, para terminar el ciclo ponga numero impar : ")
float(num)
while(float(num)%2==0):
    num=input("ingrese un numero, para terminar el ciclo ponga numero impar :  ")
