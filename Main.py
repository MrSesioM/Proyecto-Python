import Listado,Gestiones, os, time, sys, tabulate

def verde():
    print("\033[1;32;40m")
    
def blanco():
    print ("\033[1;37;40m")



def volver_menu():
    while True:
        opcion = input("\n¿Quieres volver al menu? Y/N: ")
        match opcion:
            case "y":
                os.system("cls")
                print("Volviendo al menu...")
                time.sleep(1)
                menu()
            case "n":
                os.system("cls")
                blanco()
                print("Saliendo...")
                time.sleep(1)
                os.system("cls")
                sys.exit()

            case _:
                print("\nNo has elegido una opción correcta.")
2


def menu():
    os.system("cls")
    while True:
        verde()
        menu = [["[1]", "Gestionar juegos"], ["[2]", "Mostrar informes"], ["[0]", "Salir"]]
        print(tabulate.tabulate( menu, headers=[" *","OPCIONES"], tablefmt="fancy_grid"))
        opcion = input("Introduce la tarea que quieras realizar: ")
        match opcion:
            case "1":
                os.system("cls")
                while True:
    
                    menu = [["[1]", "Dar de alta un juego"], ["[0]", "Volver"]]
                    print(tabulate.tabulate(menu, headers=["Gestionar juegos"], tablefmt="fancy_grid"))
                    #[2] |Editar un juego.      |\n
                    #[3] |Eliminar un juego.    |\n
                    
                    opcion = input("Introduce una opción: ")
                    
                    match opcion:
                        case "1":
                            print(Gestiones.alta_juegos())
                            volver_menu()

                        case "2":
                            print()
                            break
                     
                        case "3":
                            print()
                            break

                        case "0":
                            os.system("cls")
                            break
                        
                        case _:
                            print("\nNo has introducido una opción correcta.")
                            time.sleep(2)
                            os.system("cls")
            
            case "2":
                os.system("cls")
                while True:
    
                    menu = [["[1]", "Listar todos los juegos "], ["[2]", "Listar todos los editores"], ["[3]", "Listar todos los juegos del género 'Plataformas'"], ["[0]", "Volver"]]
                    print(tabulate.tabulate(menu, headers=["Mostrar informes"], tablefmt="fancy_grid"))
    
                    #[4] |Listar todos los juegos filtrados por género.                                |\n
                    #[5] |Listar todos los juegos del siglo XX.                                        |\n
                    #[6] |Listar todos los juegos publicados en años pares.                            |\n
                    #[7] |Listar todos los juego de Nintendo.                                          |\n
                    #[8] |Listar todos los juegos con mayor media de ventas.                           |\n
                    #[9] |Listar los 5 juegos mas vendidos de NA, Europa, Japón y del resto del mundo. |\n
                    opcion = input("Introduce una opción: ")
                    
                    match opcion:
                        case "1":
                            Listado.tabla_lista_juegos()
                            #Listado.ordenar_listas(Listado.listado_juegos())
                            volver_menu()

                        case "2":
                        
                            Listado.tabla_lista_editores()
                            #Listado.listado_editores()
                            volver_menu() 
                        
                        case "3":
                            Listado.tabla_juegos_plataforma()
                            #(Listado.ordenar_listas(enumerate(Listado.listado_juegos_plataformas(),1)))
                            volver_menu()

                        case "0":
                            os.system("cls")
                            break

                        case _:
                            print("\nNo has introducido una opción correcta.")
                            time.sleep(2)
                            os.system("cls")

            case "0":
                os.system("cls")
                blanco()
                print("Saliendo...")
                time.sleep(1)
                os.system("cls")
                sys.exit()
            case _:
                print("\nNo has elegido una opción correcta.")
                time.sleep(2)
                os.system("cls")
def main():

        menu()

main()
