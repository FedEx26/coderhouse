#3) Escribí un programa que sume todos los números enteros impares desde el 0 hasta el 100:
  
n = 0
sum = 0
for num in range(0, 101, 2):
    sum = sum+num
print("la sumatoria es: ", sum )