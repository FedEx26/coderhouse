 

 # funcion de año bisiesto  
def ano_bisiesto(ano):  
 # chequeo de año bisiesto 
      if((ano % 400 == 0) or  
         (ano % 100 != 0) and  
         (ano % 4 == 0)):   
        print("El año insertado es bisiesto");  
        
      # Else no es un año bisiesto  
      else:  
        print ("El año insertado NO es bisiesto")  
        
    
 
# Validacion de año
def ano():
    print('Bienvenido!!')
    try:
        ano = int(input("Ingrese un año :  "))
    except:
        print('No ingresaste un numero')
    else:
        ano_bisiesto(ano)
        
# Tomar input del usuario 
ano()