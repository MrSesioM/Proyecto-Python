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
     
    return datos

# Carga juegos en la lista con los datos obtenidos en la funcion introduce_datos
def alta_juegos():
    
    juego=introduce_datos()
    lista.append(juego)
    return lista[len(lista)-1]
  
    
leer_csv('vgsales.csv')

    