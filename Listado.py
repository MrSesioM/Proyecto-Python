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
def listado_plataformas():
    juegos_plataforma = []
    for juego in Gestiones.lista:
        if(juego[4] == "Platform"):
            juegos_plataforma.append(juego[1])
    return juegos_plataforma

# Devuelve el listado de los distintos tipos de géneros que hay
def listado_generos():
    lista_generos = []
    for juego in Gestiones.lista:
        if (juego[4] not in lista_generos):
            lista_generos.append(juego[4])
    return lista_generos

# Devuelve el listado de las plataformas que hay
def listado_consolas():
    lista_consolas = []
    for juego in Gestiones.lista:
        if (juego[2] not in lista_consolas):
            lista_consolas.append(juego[2])
    return lista_consolas
