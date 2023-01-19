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
    
<<<<<<< HEAD
    for lista in lista_plataformas:
        tabla(lista,"")

def juegos_anios_par():
    juegos_anio_par = []
    for juego in Gestiones.lista:
        if (juego[3] != "N/A"):
            if (int(juego[3]) % 2 == 0):
                juegos_anio_par.append(juego)

    for juego in juegos_anio_par:
        tabla(juego,"")

def juegos_siglo_XX():
    juegos_siglo_XX = []
    for juego in Gestiones.lista:
        if (juego[3] != "N/A"):
            if (int(juego[3]) > 1950 and int(juego[3]) < 2000):
                juegos_siglo_XX.append(juego)

    for juego in juegos_siglo_XX:
        tabla(juego,"")

def media_ventas_total():
    suma_ventas = 0
    for juego in Gestiones.lista:
        suma_ventas += float(juego[10])
    return round(suma_ventas / len(Gestiones.lista), 2)

def ventas_encima_media():
    juego_encima_media = []
    media_ventas = media_ventas_total()
    for juego in Gestiones.lista:
        if (float(juego[10]) > media_ventas):
            juego_encima_media.append(juego)

    for juego in juego_encima_media:
        tabla(juego,"")

def listado_generos():
    lista_generos = []
    for juego in Gestiones.lista:
        if (juego[4] not in lista_generos):
            lista_generos.append(juego[4])
    return lista_generos

def juegos_por_genero():
    genero = ""
    while (genero not in listado_generos()):
        genero = input(f"Introduce el género ({listado_generos()}: ")
    else:
        juegos_genero = []
        for juego in Gestiones.lista:
            if (genero == juego[4]):
                juegos_genero.append(juego)

    for juego in juegos_genero:
        tabla(juego,"")

def naranja():
    print("\033[33m")

def verde():
    print("\033[1;32;40m")
    
def blanco():
    print("\033[1;37;40m")
=======
    return cinco_juegos_vendidos
>>>>>>> d463f11f3ffc107a9e03e205625dad629e9d5dee
