import Gestiones,tabulate

# Devuelve el listado de todos los juegos
def listado_juegos():
   return Gestiones.lista


# Devuelve el listado de los editores de los juegos  
def listado_editores():
    lista_editores = []
    for juego in Gestiones.lista:
        if (juego[5] not in lista_editores):
            lista_editores.append(juego[5])
    return lista_editores

# Devuelve el listado de los juegos que son de genero plataforma
def listado_juegos_plataformas():
    juegos_plataforma = []
    for juego in Gestiones.lista:
        if(juego[4] == "Platform"):
            juegos_plataforma.append(juego[1])
    return juegos_plataforma

#def ordenar_listas(lista):
   # for i in lista:
    #    print(f"Rank: {i[j]}, Nombre: {i[j+1]}, Plataforma: {i[2]}, Año: {i[3]}, Genero: {i[4]}, Publisher: {i[5]}, Ventas NA: {i[6]}, Ventas EU: {i[7]}, Ventas JP: {i[8]}, Otras ventas: {i[9]}, Ventas global: {i[10]}")
        

def tabla(lista): #Crea una tabla a partir de una estructura de listas
    
    menu = [lista]
    print(tabulate.tabulate(menu,tablefmt="fancy_grid"))


def tabla_lista_juegos(): #Crea una tabla a de listado_juegos
    
    for juego in Gestiones.lista:
        tabla(juego)

def tabla_lista_editores(): #Crea una tabla de listado_editores

    lista_editores = []
    for editor in listado_editores():
        lista_editores.append([editor])
    
    for lista in lista_editores:
        tabla(lista)

def tabla_juegos_plataforma(): #Crear una tabla de listado_juegos_plataformas()

    lista_plataformas = []
    for juegos in listado_editores():
        lista_plataformas.append([juegos])
    
    for lista in lista_plataformas:
        tabla(lista)

