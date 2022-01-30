alumno=input("Ingrese nombre del Alumno:  ")
nota_1=input("Ingrese la Nota 1 de "+ alumno+" :")
print("Nota1:  "+nota_1)
nota_2=input("Ingrese la Nota 2 de "+ alumno+" :  ")
print("Nota2:  "+ nota_2)
nota_3=input("Ingrese la Nota 3 de "+ alumno+" :  ")
print("Nota2:  "+ nota_2)
nota_1=float(nota_1)*0.15
nota_2=float(nota_2)*0.35
nota_3=float(nota_3)*0.5
nota_final=nota_1+nota_2+nota_3
print("La nota media del Alumno " +alumno+ "   es   "+str(nota_final))