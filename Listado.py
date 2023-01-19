import Gestiones



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


def cinco_juegos_mas_vendidos():
    
    lista_juegos_vendidos = []
    cinco_juegos_vendidos = []

    for ventas in Gestiones.lista:
        lista_juegos_vendidos.append(ventas)
    
    lista_juegos_vendidos.sort(key=lambda x: x[10], reverse=True) # Ordenar la lista de juegos de mayor a menor
    lista_juegos_vendidos.remove(lista_juegos_vendidos[0])
    
    for i in range(5):     # Imprimir los 5 juegos más vendidos
        cinco_juegos_vendidos.append(lista_juegos_vendidos[i])
    
    return cinco_juegos_vendidos