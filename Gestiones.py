import csv,os,Listado,time


lista=[]
#Carga el fichero csv en la lista

def leer_csv(archivo):

    with open(archivo) as juegos:

        # Utilizamos la libreria csv para leer el archivo y lo guardamos en una variable llamada reader
        reader = csv.reader(juegos, delimiter=',')

        # Recorremos todas las lineas del archivo con un for y guardamos los datos en la lista lista[] que creamos antes
        for row in reader:
            lista.append(row)

# Compruebo si la plataforma, el género o el desarrollador ya existen o no, y si queremos añadir uno nuevo
def comprobacion(datos,pregunta,i):

    while True:
        try:
            if pregunta == "Platform":
                listado = [x.lower() for x in Listado.listado_consolas()]
                texto = "No has introducido una plataforma existente, ¿Quieres introducir una nueva? (y/n): "
            elif pregunta == "Genre":
                listado = [x.lower() for x in Listado.listado_generos()]
                texto = "No has introducido un género existente, ¿Quieres introducir uno nuevo? (y/n): "
            elif pregunta == "Publisher":
                listado = [x.lower() for x in Listado.listado_editores()]
                texto = "No has introducido una desarrolladora existente, ¿Quieres introducir una nueva? (y/n): "

            datos.append(input(f"Introduce el {pregunta}: "))

            assert datos[i].lower() in listado, texto
            datos.insert(i, (datos[i].lower()).capitalize())
            datos.pop()
            
        except AssertionError as texto:
            datos.pop()
            respuesta = (input(texto)).lower()
            while respuesta != "y" and respuesta != "n":
                respuesta = input("Tienes que introducir y o n: ")
            if respuesta.lower() == "y":
                datos.append((input(f"Introduce el {pregunta}: ")).capitalize())
                break
            elif respuesta.lower() == "n":
                continue
            else:
                break
        else:
            break
    return datos

# Compruebo si se introduce un número válido en las ventas o si queremos dejarlo en blanco
def ventas():
    while True:
        try:
            ventas = input("Introduce el nº de ventas (en millones) (dejar en blanco si se desconoce): ")
            if ventas == "":
                return ventas
            else:
                ventas = float(ventas)
                return ventas
        except ValueError:
            print("No has introducido un número válido.")
        

# Funcion auxiliar par pedir datos
def introduce_datos():
    datos = []
    lista_preguntas = ['Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
    floats = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
    for i in range(len(lista_preguntas)):
        while True:
            if lista_preguntas[i] == "Name":
                try:
                    datos.append(input(f"\nIntroduce el {lista_preguntas[i]}: "))
                    assert datos[i] != "", "El nombre no puede estar vacío."
                except AssertionError as error:
                    print(error)
                    datos.pop()
                else:
                    break
            # Compruebo si se introduce un dato válido en Year (un número entero mayor a 1958)
            elif lista_preguntas[i] == "Year":
                try:
                    datos.append(int(input(f"Introduce el {lista_preguntas[i]}: ")))
                    assert datos[i] >= 1958 and datos[i] <= 2023, "El año de lanzamiento tiene que estar entre 1958 y 2023."

                except ValueError:
                    print("No has introducido un número válido")
                except AssertionError as error:
                    print(error)
                    datos.pop()
                else:
                    break
            # Compruebo si se introduce un dato válido en Genre, Publisher o Platform y añadir la posibilidad de crear uno nuevo en caso de que no exista
            elif lista_preguntas[i] == "Platform":
                comprobacion(datos,lista_preguntas[i],i)
                break

            elif lista_preguntas[i] == "Genre":
                comprobacion(datos,lista_preguntas[i],i)
                break

            elif lista_preguntas[i] == "Publisher":
                comprobacion(datos,lista_preguntas[i],i)
                break
                
            elif lista_preguntas[i] in floats:
                datos.append(ventas())
                break
            else:
                datos.append(input(f"Introduce el {lista_preguntas[i]}: "))
                break
    rank = len(lista) + 2
    datos.insert(0, rank)
    os.system("cls")

    return datos

# Carga juegos en la lista con los datos obtenidos en la funcion introduce_datos
def alta_juegos():
    juego=introduce_datos()
    lista.append(juego)
    salida = ("Nombre del juego: ","Plataforma: ","Año de lanzamiento: ","Género: ","Desarrolladora: ","Nº de ventas en América del Norte (en millones): ","Nº de ventas en Europa (en millones): ","Nº de ventas en Japón (en millones): ","Nº de ventas en otros países (en millones): ","Nº de ventas globales (en millones): ")
    resultado = ""
    for i in range(len(salida)):
        if juego[i+1] == "":
            resultado += (f"{i+1} - {salida[i]}desconocido.\n")
        else:
            resultado += (f"{i+1} - {salida[i]}{juego[i+1]}\n")
    return resultado


def editar_juegos():
    while True:
        nombre = input("Escribe el juego que quiere editar (0 para salir): ")
        if nombre == "0":
            break
        juego = ""
        for i in lista:
            if nombre.lower() == i[1].lower():
                juego = i
                while True:
                    print("\nEstos son los datos del juego:\n",juego)
                    editar = input("\n¿Que quiere editar de este juego? (Rank, Name, Platform, Year, Genre, Publisher, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales) (Introduce 0 para salir)\n")
                    match editar:
                        case "rank":
                            while True:
                                try:
                                    rango = int(input("\nIntroduce el nuevo rango: "))
                                    for i in lista:
                                        assert str(rango) != i[0], "\nEse rango ya existe."
                                
                                except ValueError:
                                    print("\nEl rango tiene que ser un número entero.")
                                except AssertionError as msg:
                                    print(msg)
                                else:
                                    juego[0] = str(rango)
                                    break


                        case "name":
                            nombre = input("\nIntroduce el nuevo nombre: ")
                            juego[1] = nombre.capitalize()


                        case "platform":
                            plataforma = []
                            juego[2] = comprobacion(plataforma,"Platform",0)[0]
                            
                        case "year":
                            while True:
                                try:
                                    año = int(input("Introduce el año de lanzamiento: "))
                                    assert año >= 1958 and año <= 2023, "El año de lanzamiento tiene que estar entre 1958 y 2023."
                                except ValueError:
                                    print("No has introducido un número válido")
                                except AssertionError as error:
                                    print(error)
                                else:
                                    juego[3] = año
                                    break
                            
                        case "genre":
                            genero = []
                            juego[4] = comprobacion(genero,"Genre",0)[0]
                            
                        case "publisher":
                            desarrolladora = []
                            juego[5] = comprobacion(desarrolladora,"Publisher",0)[0]

                        case "na_sales":
                            juego[6] = ventas()
                        
                        case "eu_sales":
                            juego[7] = ventas()

                        case "jp_sales":
                            juego[8] = ventas()

                        case "other_sales":
                            juego[9] = ventas()

                        case "global_sales":
                            juego[10] = ventas()
                        
                        case "0":
                            break

                        case _:
                            print("Has introducido una opción no válida.")

        if juego == "":
            pregunta = input("Ese juego no se encuentra, ¿quieres añadirlo? (y/n)\n")
            while True:
                if pregunta == "y":
                    print(f"Has añadido el siguiente juego:\n{alta_juegos()}")
                    break
                elif pregunta == "n":
                    break
                else:
                    pregunta = input("Tienes que introducir y o n para continuar: ")
        else:
            print("Has hecho cambios en este juego:\n")
            return juego
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
