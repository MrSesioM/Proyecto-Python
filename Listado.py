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
    return ordenar_editores(lista_editores)

# Devuelve el listado de los juegos que son de genero plataforma
def listado_juegos_plataformas():
    juegos_plataforma = []
    for juego in Gestiones.lista:
        if(juego[4] == "Platform"):
            juegos_plataforma.append(juego[1])
    return juegos_plataforma

def ordenar_listas(lista):
    for i in lista:
        print(f"Rank: {i[0]}, Nombre: {i[1]}, Plataforma: {i[2]}, Año: {i[3]}, Genero: {i[4]}, Publisher: {i[5]}, Ventas NA: {i[6]}, Ventas EU: {i[7]}, Ventas JP: {i[8]}, Otras ventas: {i[9]}, Ventas global: {i[10]}")
        
def ordenar_editores(lista):
    for i in lista:
        print(i)