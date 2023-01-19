import csv, os, time


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
    lista_preguntas = ['Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
    floats = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
    strings = ['Genre', 'Publisher']
    for i in range (len(lista_preguntas)):
        while True:
            # Compruebo si se introduce un dato válido en Year (un número entero mayor a 1958)
            if lista_preguntas[i] == "Year":
                try:
                    datos.append(int(input(f"Introduce el {lista_preguntas[i]}: ")))
                    assert datos[i] >= 1958, "No puedes introducir un año menor a 1958."
                
                except ValueError:
                    print("No has introducido un número válido")
                except AssertionError as error:
                    print(error)
                    datos.pop()
                else:
                    break
            # Compruebo si se introduce un dato válido en Genre o Publisher (que no sea un número o un float, tiene que contener caracteres)
            elif lista_preguntas[i] =='Genre' or 'Publisher' :
                try:
                    datos.append(input(f"Introduce el {lista_preguntas[i]}: "))
                    datos[i] = float(datos[i])
                except ValueError:
                    break
                else:
                    print("No puedes introducir solamente un número.")
                    datos.pop()
            # Compruebo si se introduce 
            elif lista_preguntas[i] in floats:
                try:
                    datos.append(float(input(f"Introduce el {lista_preguntas[i]}: ")))            
                    print("No has introducido un número válido")
                except:
                    break
            else:
                datos.append(input(f"Introduce el {lista_preguntas[i]}: "))
                break
    rank = len(lista) + 2
    datos.insert(0, rank)
     
    return datos

# Carga juegos en la lista con los datos obtenidos en la funcion introduce_datos
def alta_juegos():
    
    juego=introduce_datos()
    lista.append(juego)
    return lista[len(lista)-1]

# La funcion elimina los juegos de la lista comprobando el nombre del juego y la plataforma 
def eliminar_juegos():
    salir = True
    while salir:
        juegos_eliminar = input("Que juego quieres eliminar: ")
        plataforma_juegos = input("De que plataforma es tu juego: ")
        for i in lista:
                if juegos_eliminar.lower() == i[1].lower() and plataforma_juegos.lower() == i[2].lower():
                    confirmacion = input("Estas seguro Y/N: ")

                    if confirmacion == "y":
                            lista.remove(i)
                            os.system("cls")
                            print("Has eliminado el juego\n",i)
                            time.sleep(2)
                            os.system("cls")
                            salir = False

                    elif confirmacion == "n":
                            os.system("cls") 
                            print("No has eliminado ningun juego")
                            time.sleep(2)
                            os.system("cls")
                            salir = False
                            
                    
                


leer_csv('vgsales.csv')
#introduce_datos()


       

