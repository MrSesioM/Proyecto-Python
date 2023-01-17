import csv

def lista_csv():

    lista=[]
    with open('vgsales.csv') as juegos:

        # Utilizamos la libreria csv para leer el archivo y lo guardamos en una variable llamada reader. 
        reader = csv.reader(juegos, delimiter=',')

        # Recorremos todas las lineas del archivo con un for y guardamos los datos en la lista lista[] que creamos antes. 
        for row in reader:
            lista.append(row)     

        # Imprimimos la lista para verificar que los datos se hayan guardado correctamente. 
        print(lista)
    return lista


lista = lista_csv()




def introduce_datos():

    datos = []
    lista =['Rank', 'Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
    for i in range (len(lista)):
        
        datos.append(input(f"Introduce el {lista[i]}: "))
     
    return datos


def alta_juegos():
    
    juego=introduce_datos()
    lista.append(juego)
    return lista[len(lista)-1]
  
    
   