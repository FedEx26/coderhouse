#from typing import List
matriz = [ [1, 1, 1],
[2, 2, 2],
[3, 3, 3],
[4, 4, 4]]

a=sum(matriz[0])
b=sum(matriz[1])
c=sum(matriz[2])
d=sum(matriz[3])
matriz.insert(1,a)
matriz.insert(3,b)
matriz.insert(5,c)
matriz.insert(7,d)
print(matriz)


#print(sum(matriz[0]))
#print(sum(matriz[1]))
#print(sum(matriz[2]))
#print(sum(matriz[3]))

#matriz.append(sum(matriz[0]))