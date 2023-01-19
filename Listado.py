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
    for editor in listado_editores():
        lista_editores.append([editor])
    
    for lista in lista_editores:
        tabla(lista,"")

def tabla_juegos_plataforma(): #Crear una tabla de listado_juegos_plataformas()

    lista_plataformas = []
    for juegos in listado_editores():
        lista_plataformas.append([juegos])
    
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