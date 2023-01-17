
    

# Se inicializa la variable que almacenará los 11 valores
valores = []

# Se utiliza un bucle for para solicitar los 11 valores al usuario
for i in range(11):
    try:
        # Se solicita el valor al usuario y se agrega a la lista de valores
        valor = int(input("Introduzca el número {}: ".format(i+1))) 
        valores.append(valor)

    # Si el usuario introduce un dato no numérico, se muestra un mensaje de error y se vuelve a solicitar el dato    
    except ValueError: 
        print("Error, debe introducir un número entero.") 

        # Se decrementa el contador para volver a solicitar el mismo número al usuario 
        i -= 1  

    # Al final del bucle for, la lista 'valores' contendrá los 11 valores introducidos por el usuario.