import Gestiones, Listado, tabulate

def tabla(lista,header): #Crea una tabla a partir de una estructura de listas
    
    naranja()
    menu=[lista]
    print(tabulate.tabulate(menu,header,stralign="center",tablefmt="fancy_grid"))

    
def tabla_lista_juegos(): #Crea una tabla a de listado_juegos
    
    header=['Rank','Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales (mill)', 'EU_Sales (mill)', 'JP_Sales (mill)', 'Other_Sales (mill)', 'Global_Sales (mill)']
    for juego in Gestiones.lista:
        tabla(juego,header)

def tabla_lista_editores(): #Crea una tabla de listado_editores

    lista_editores = []
    for editor in Listado.listado_editores():
        lista_editores.append([editor])
    
    for lista in lista_editores:
        tabla(lista,"")

def tabla_juegos_plataforma(): #Crear una tabla de listado_juegos_plataformas()

    lista_plataformas = []
    for juegos in Listado.listado_editores():
        lista_plataformas.append([juegos])
    
    for lista in lista_plataformas:
        tabla(lista,"")

def tabla_juegos_nitendo():
    lista_nintendo = []
    header=['Rank','Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales (mill)', 'EU_Sales (mill)', 'JP_Sales (mill)', 'Other_Sales (mill)', 'Global_Sales (mill)']
    for juegos in Listado.listado_juegos_nintendo():
        lista_nintendo.append([juegos])
    
    for lista in lista_nintendo:
        tabla(lista,"")


def tabla_cinco_juegos_mas_vendidos(): #Crear una tabla de los 5 juegos mas vendidos
    header=['Rank','Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales (mill)', 'EU_Sales (mill)', 'JP_Sales (mill)', 'Other_Sales (mill)', 'Global_Sales (mill)']
    for juego in Listado.cinco_juegos_mas_vendidos():
        tabla(juego,header)

def tabla_juegos_anios_par():
    juegos_anio_par = []
    for juego in Gestiones.lista:
        if (juego[3] != "N/A"):
            if (int(juego[3]) % 2 == 0):
                juegos_anio_par.append(juego)

    for juego in juegos_anio_par:
        tabla(juego,"")

def tabla_juegos_siglo_XX():
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

def tabla_ventas_encima_media():
    juego_encima_media = []
    media_ventas = media_ventas_total()
    for juego in Gestiones.lista:
        if (float(juego[10]) > media_ventas):
            juego_encima_media.append(juego)

    for juego in juego_encima_media:
        tabla(juego,"")


def tabla_juegos_por_genero():
    genero = ""
    while (genero not in Listado.listado_generos()):
        genero = input(f"Introduce el género ({Listado.listado_generos()}: ")
        
    juegos_genero = []
    for juego in Gestiones.lista:
        if (genero == juego[4]):
            juegos_genero.append(juego)
    for juego in juegos_genero:
        tabla(juego,"")

def listado_generos():
    lista_generos = []
    for juego in Gestiones.lista:
        if (juego[4] not in lista_generos):
            lista_generos.append(juego[4])
    return lista_generos

def naranja():
    print("\033[33m")

def verde():
    print("\033[1;32;40m")
    
def blanco():
    print("\033[1;37;40m")

def rojo():
    print("\033[1;31;40m")

def morado():
    print("\033[35m")