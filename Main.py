import Listado,Gestiones, os, time, sys



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
                print("Saliendo...")
                time.sleep(1)
                sys.exit()

            case _:
                print("\nNo has elegido una opción correcta.")



def menu():
    os.system("cls")
    while True:
        
        print("""\n[A] |Gestionar juegos.|\n
[B] |Mostar informes. |\n
[0] |Salir.           |\n""")
        opcion = input("Introduce la tarea que quieras realizar: ")
        match opcion:
            case "a":
                os.system("cls")
                while True:
    
                    print("""\n[1] |Dar de alta un juego. |\n
[2] |Editar un juego.      |\n
[3] |Eliminar un juego.    |\n
[0] |Volver.               |\n""")
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
                            break
                        
                        case _:
                            print("\nNo has introducido una opción correcta.")
                            time.sleep(2)
                            os.system("cls")
            
            case "b":
                os.system("cls")
                while True:
    
                    print("""[1] |Listar todos los juegos                                                      |\n
[2] |Listar todos los editores                                                    |\n
[3] |Listar todos los juegos del género 'Plataformas'.                            |\n
[4] |Listar todos los juegos filtrados por género.                                |\n
[5] |Listar todos los juegos del siglo XX.                                        |\n
[6] |Listar todos los juegos publicados en años pares.                            |\n
[7] |Listar todos los juego de Nintendo.                                          |\n
[8] |Listar todos los juegos con mayor media de ventas.                           |\n
[9] |Listar los 5 juegos mas vendidos de NA, Europa, Japón y del resto del mundo. |\n
[0] |Volver.                                                                      |\n""")

                    opcion = input("Introduce una opción: ")
                    
                    match opcion:
                        case "1":
                            Listado.ordenar_listas(Listado.listado_juegos())
                            volver_menu()

                        case "2":
                            Listado.listado_editores()
                            volver_menu() 
                        
                        case "3":
                            (Listado.ordenar_listas(enumerate(Listado.listado_juegos_plataformas(),1)))
                            volver_menu()

                        case "0":
                            break

                        case _:
                            print("\nNo has introducido una opción correcta.")
                            time.sleep(2)
                            os.system("cls")

            case "0":
                break

            case _:
                print("\nNo has elegido una opción correcta.")
                time.sleep(2)
                os.system("cls")
def main():

        menu()

main()
