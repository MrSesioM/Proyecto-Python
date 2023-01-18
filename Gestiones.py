import csv


lista=[]
#Carga el fichero csv en la lista

def leer_csv(archivo):

    with open(archivo) as juegos:

        # Utilizamos la libreria csv para leer el archivo y lo guardamos en una variable llamada reader. 
        reader = csv.reader(juegos, delimiter=',')

        # Recorremos todas las lineas del archivo con un for y guardamos los datos en la lista lista[] que creamos antes. 
        for row in reader:
            lista.append(row)

# Funcion auxiliar par pedir datos
def introduce_datos():
    datos = []
    datos.append(len(lista))
    datos_introducir = ['Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
    for i in range (len(datos_introducir)):
        
        datos.append(input(f"Introduce el {datos_introducir[i]}: "))
    lista =['Rank', 'Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
    floats = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
    strings = ['Genre', 'Publisher']
    for i in range (len(lista)):
        while True:
            # Compruebo si se introduce un dato válido en Year (un número entero mayor a 1958)
            if lista[i] == "Year":
                try:
                    datos.append(int(input(f"Introduce el {lista[i]}: ")))
                    assert datos[i] >= 1958, "No puedes introducir un año menor a 1958."
                except ValueError:
                    print("No has introducido un número válido")
                except AssertionError as error:
                    print(error)
                    datos.pop()
                else:
                    break
            # Compruebo si se introduce un dato válido en Genre o Publisher (que no sea un número o un float, tiene que contener caracteres)
            elif lista[i] in strings:
                try:
                    datos.append(input(f"Introduce el {lista[i]}: "))
                    datos[i] = float(datos[i])
                except ValueError:
                    break
                else:
                    print("No puedes introducir solamente un número.")
                    datos.pop()
            # Compruebo si se introduce 
            elif lista[i] in floats:
                try:
                    datos.append(float(input(f"Introduce el {lista[i]}: ")))            
                except ValueError:
                    print("No has introducido un número válido")
                else:
                    break
            else:
                datos.append(input(f"Introduce el {lista[i]}: "))
                break
            
     
    return datos

# Carga juegos en la lista con los datos obtenidos en la funcion introduce_datos
def alta_juegos():
    
    juego=introduce_datos()
    lista.append(juego)
    return lista[len(lista)-1]
  
introduce_datos()
leer_csv('vgsales.csv')

    