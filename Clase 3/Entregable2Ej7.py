lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

#Dadas 2 listas, debes generar una tercera lista con todos los elementos que se repitan en ellas, pero no debe repetirse ningún elemento en la nueva lista:

lista_3 = lista_1 + lista_2
print(lista_3)
lista_3=list(dict.fromkeys(lista_3))
print(lista_3)