import Gestiones, tabulate, Tablas



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


def cinco_juegos_mas_vendidos(): #Devuelve una lista con los 5 jeugos mas vendidos

    lista_juegos_vendidos = []
    cinco_juegos_vendidos = []

    for ventas in Gestiones.lista:
        lista_juegos_vendidos.append(ventas)

    lista_juegos_vendidos.sort(key=lambda x: x[10], reverse=True) # Ordenar la lista de juegos de mayor a menor

    for i in range(5):     # Imprimir los 5 juegos más vendidos
        cinco_juegos_vendidos.append(lista_juegos_vendidos[i])

    return cinco_juegos_vendidos

# Devuelve el listado de los juego que son de la compañia nintendo

def listado_juegos_nintendo():
    juegos_nintendo = []
    for juego in Gestiones.lista:
        if juego[5] == "Nintendo":
            juegos_nintendo.append(juego)
    return juegos_nintendo


def listado_generos():
    lista_generos = []
    for juego in Gestiones.lista:
        if (juego[4] not in lista_generos):
            lista_generos.append(juego[4])
    return lista_generos
