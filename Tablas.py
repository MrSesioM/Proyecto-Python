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

def tabla_juegos_nintendo(): #Crear una tabla de los juegos de nintendo
    lista_nintendo = []
    header=['Rank','Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales (mill)', 'EU_Sales (mill)', 'JP_Sales (mill)', 'Other_Sales (mill)', 'Global_Sales (mill)']
    for juegos in Listado.listado_juegos_nintendo():
        tabla(juegos,header)
    
def tabla_cinco_juegos_mas_vendidos(): #Crear una tabla de los 5 juegos mas vendidos
    header=['Rank','Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales (mill)', 'EU_Sales (mill)', 'JP_Sales (mill)', 'Other_Sales (mill)', 'Global_Sales (mill)']
    for juego in Listado.cinco_juegos_mas_vendidos():
        tabla(juego,header)

def tabla_juegos_anios_par():   #Crear una tabla de los juegos de año par
    juegos_anio_par = []
    for juego in Gestiones.lista:
        if (juego[3] != "N/A"):
            if (int(juego[3]) % 2 == 0):
                juegos_anio_par.append(juego)

    for juego in juegos_anio_par:
        tabla(juego,"")

def tabla_juegos_siglo_XX():    #Crear una tabla de los juegos sigo XX
    juegos_siglo_XX = []
    for juego in Gestiones.lista:
        if (juego[3] != "N/A"):
            if (int(juego[3]) > 1950 and int(juego[3]) < 2000):
                juegos_siglo_XX.append(juego)

    for juego in juegos_siglo_XX:
        tabla(juego,"")

def media_ventas_total():   #Retorna la media de la ventas globales
    suma_ventas = 0
    for juego in Gestiones.lista:
        suma_ventas += float(juego[10])
    return round(suma_ventas / len(Gestiones.lista), 2)

def tabla_ventas_encima_media():    #Crear una tabla de los juegos en ventas por encima de la media
    juego_encima_media = []
    media_ventas = media_ventas_total()
    for juego in Gestiones.lista:
        if (float(juego[10]) > media_ventas):
            juego_encima_media.append(juego)

    for juego in juego_encima_media:
        tabla(juego,"")

def tabla_juegos_por_genero():  #Crear una tabla de los juegos filtrados por genero
    genero = ""
    while (genero not in Listado.listado_generos()):
        
        tabla(Listado.listado_generos(),"")
        verde()
        genero = input("Introduce el género: ")
        
    juegos_genero = []
    for juego in Gestiones.lista:
        if (genero == juego[4]):
            juegos_genero.append(juego)
    for juego in juegos_genero:
        tabla(juego,"")

def tabla_paginada():   #Crear una tabla paginada (testing)

    import pandas as pd
    header=['Rank','Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales (mill)', 'EU_Sales (mill)', 'JP_Sales (mill)', 'Other_Sales (mill)', 'Global_Sales (mill)']
    df = pd.DataFrame(Gestiones.lista, columns=header)
    #paginar la lista
    paginado = df.iloc[::2]
    print(paginado)


#def Colores(color):

def naranja():  #Color naranja
    print("\033[33m")

def verde():    #Color verde
    print("\033[1;32;40m")
    
def blanco():   #Color blanco
    print("\033[1;37;40m")

def rojo(): #Color rojo
    print("\033[1;31;40m")

def morado():   #Color morado
    print("\033[35m")