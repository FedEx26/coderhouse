# 6) Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares, y la segunda con los números impares:
# 🖐 Ayuda: Para ordenar una lista automáticamente puedes usar el método .sort()
listapar=[]
listaimpar=[]
lista1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def separar():
    for i in lista1:
        if i == 0:
            listapar.append(i)

        elif i%2 == 0:

            listapar.append(i)

        else:
            listaimpar.append(i)

separar()
print(listapar)
print(listaimpar)