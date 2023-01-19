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


# Devuelve el listado de los juego que son de la compañia nintendo

def listado_juegos_nintendo():
    juegos_nintendo = []
    for juego in Gestiones.lista:
        if juego[5] == "Nintendo":
            juegos_nintendo.append(juego)
    return juegos_nintendo


