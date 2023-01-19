import Gestiones, Listado, tabulate 
import pandas as pd

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

def tabla_cinco_juegos_mas_vendidos():
    header=['Rank','Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales (mill)', 'EU_Sales (mill)', 'JP_Sales (mill)', 'Other_Sales (mill)', 'Global_Sales (mill)']
    for juego in Listado.cinco_juegos_mas_vendidos():
        tabla(juego,header)

def naranja():
    print("\033[33m")

def verde():
    print("\033[1;32;40m")
    
def blanco():
    print("\033[1;37;40m")