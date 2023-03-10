import Listado, Gestiones, os, time, sys, tabulate, Tablas, csv

def guardar_cambios():  #Guarda los cambios de lista en un fichero

    
    if Gestiones.lista_guardar!=Gestiones.lista:
        opcion_guardar= input("\n¿Quieres guardar los cambios? Y/N: ")
        match opcion_guardar:
            case "y":
                os.system("cls")
                Tablas.blanco()
                with open("vgsales2.csv", "w") as f:
                    writer = csv.writer(f)
                    for juego in Gestiones.lista:
                        with open("vgsales2.csv", "a") as f2:
                            writer2 = csv.writer(f)
                            writer2.writerow(juego)
                print("Guardando...")
                time.sleep(1)
                print("Saliendo...")
                time.sleep(1)
                sys.exit()
                
            case "n":
                os.system("cls")
                Tablas.blanco()
                print("Saliendo...")
                time.sleep(1)
                os.system("cls")
                sys.exit()

            case _:
                Tablas.rojo()
                print("\nNo has elegido una opción correcta.")
                Tablas.blanco()
    else:
        os.system("cls")
        print("No hay cambios que guardar...")
        time.sleep(1)
        Tablas.blanco()
        print("Saliendo...")
        time.sleep(1)
        os.system("cls")
        sys.exit()

def testing():  #Funcion par acceder a menu_testinf() segun unas condiciones
    import getpass
    os.system("cls")
    Tablas.morado()
    password=getpass.getpass("Has entrado en el modo testing...\n\nIntroduce la password: ")
    if(password == "testing"):
        menu_testing()
    else:
        Tablas.rojo()
        print("\nPassword incorrecta!")
        time.sleep(2)
        os.system("cls")

def menu_testing():  #Accede al menu de testeo (solo admin)
    
    os.system("cls")
    while True:
        menu_test = [["[1]", "Ejecutar pruebas"],["[2]", "Ejecutar prueba sobre introduce_datos()"],["[3]", "Listar juegos (Pandas)"],["[0]", "Salir"]]
        print(tabulate.tabulate(menu_test, headers=[" *","MODO TESTING "], tablefmt="fancy_grid"))
        opcion = input("\nIntroduce una opción: ")
        match opcion:
                    case "1":
                        os.system("cls")
                        print("MODO TESTING\n")
                        os.system(r"python -m unittest C:\Users\Varito\Documents\Proyecto\_tests\_ttest_proyecto.py")
                        time.sleep(3)
                        volver_menu_guardar()
                    case "2":
                        os.system("cls")
                        print("MODO TESTING\n")
                        os.system(r"python -m unittest C:\Users\Varito\Documents\Proyecto\_tests\_ttest_introduce_datos.py")
                        time.sleep(3)
                        volver_menu_guardar()

                    case "3":
                        Tablas.tabla_paginada()
                        time.sleep(2)
                        volver_menu_guardar()
                    case "0":
                        os.system("cls")    
                        volver_menu_guardar()
                    case _:
                        Tablas.rojo()
                        print("\nNo has elegido una opción correcta.")
                        Tablas.morado()
                        time.sleep(2)
                        os.system("cls")
                
def volver_menu_guardar():  #Llama a la funcion menu() pero incluyendo la funcion guardar_cambios()
    while True:
        Tablas.blanco()
        opcion = input("\n¿Quieres volver al menu? Y/N: ")
        match opcion:
            case "n":
                os.system("cls")
                Tablas.blanco()
                guardar_cambios()
                print("Volviendo al menu...")
                time.sleep(1)
                menu()

            case "y":
                os.system("cls")
                Tablas.blanco()
                time.sleep(1)
                os.system("cls")
                menu()

            case _:
                Tablas.rojo()
                print("\nNo has elegido una opción correcta.")
                Tablas.blanco()

def menu(): #Muestra unas opciones para realizar tareas especificas sobre lista
    os.system("cls")
    while True:
        Tablas.verde()
        menu = [["[1]", "Gestionar juegos"], ["[2]", "Mostrar informes"], ["[0]", "Salir"]]
        print(tabulate.tabulate(menu, headers=[" *","OPCIONES"],tablefmt="fancy_grid"))
        opcion = input("\nIntroduce la tarea que quieras realizar: ")
        match opcion:
            case "1":
                os.system("cls")
                while True:
                    Tablas.verde()
                    menu = [["[1]", "Dar de alta un juego"],["[2]", "Editar un juego"],["[3]","Eliminar un juego"],["[0]", "Volver"]]
                    print(tabulate.tabulate(menu, headers=[" *","Gestionar juegos"], tablefmt="fancy_grid"))
                    header = ['Rank','Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales (mill)', 'EU_Sales (mill)', 'JP_Sales (mill)', 'Other_Sales (mill)', 'Global_Sales (mill)']
                    opcion = input("\nIntroduce una opción: ")
                    
                    match opcion:
                        case "1":
                            Tablas.tabla(Gestiones.alta_juegos(),header)
                            volver_menu_guardar()

                        case "2":
                            Tablas.tabla(Gestiones.editar_juegos(),header)
                            volver_menu_guardar()
                     
                        case "3":
                            
                            if Gestiones.eliminar_juegos() == False:
                                volver_menu()
                            else:   
                                Tablas.tabla(Gestiones.eliminar_juegos(),header)
                                volver_menu_guardar()

                        case "0":
                            os.system("cls")
                            break
                        
                        case _:
                            Tablas.rojo()
                            print("\nNo has elegido una opción correcta.")
                            time.sleep(2)
                            os.system("cls")
            
            case "2":
                os.system("cls")
                while True:
                    Tablas.verde()
                    menu = [["[1]", "Listar todos los juegos "], 
                        ["[2]", "Listar todos los editores"], 
                        ["[3]", "Listar todos los juegos del género 'Plataformas'"],
                        ["[4]","Listar todos los juegos filtrados por género"],
                        ["[5]","Listar todos los juegos del siglo XX"],
                        ["[6]","Listar todos los juegos publicados en años pares"],
                        ["[7]","Listar todos los juego de Nintendo"],
                        ["[8]","Listar todos los juegos con mayor media de ventas"],
                        ["[9]","Listar los 5 juegos mas vendidos de NA, Europa, Japón y del resto del mundo"], 
                        ["[0]", "Volver"]]
                    print(tabulate.tabulate(menu, headers=[" *","Mostrar informes"], tablefmt="fancy_grid"))
    
                   
                    opcion = input("\nIntroduce una opción: ")
                    
                    match opcion:
                        case "1":
                            Tablas.tabla_lista_juegos()
                            volver_menu_guardar()

                        case "2":
                            Tablas.tabla_lista_editores()
                            volver_menu_guardar() 
                        
                        case "3":
                            Tablas.tabla_juegos_plataforma()
                            volver_menu_guardar()
                        
                        case "4":
                            Tablas.tabla_juegos_por_genero()   
                            volver_menu_guardar()
                        
                    
                        case "5":
                            Tablas.tabla_juegos_siglo_XX()
                            volver_menu_guardar()

                        case "6":
                            Tablas.tabla_juegos_anios_par()
                            volver_menu_guardar()

                        case "7":
                            Tablas.tabla_juegos_nintendo()
                            volver_menu_guardar()

                        case "8":
                            Tablas.tabla_ventas_encima_media()
                            volver_menu_guardar()

                        case "9":
                            Tablas.tabla_cinco_juegos_mas_vendidos()
                            volver_menu_guardar()

                        case "0":
                            os.system("cls")
                            break

                        case _:
                            Tablas.rojo()
                            print("\nNo has elegido una opción correcta.")
                            time.sleep(2)
                            os.system("cls")

            case "0":
                os.system("cls")
                Tablas.blanco()
                guardar_cambios()
                print("Saliendo...")
                time.sleep(1)
                os.system("cls")
                sys.exit()
            
            case "admin":
                testing()
                volver_menu_guardar()
            
            case _:
                Tablas.rojo()
                print("\nNo has elegido una opción correcta.")
                Tablas.blanco()
                time.sleep(2)
                os.system("cls")
                       
def main(): #Funcion main()-->llama a menu()
    menu()

main()

#Render text