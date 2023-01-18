import Listado,Gestiones

def menu():
    while True:
        print("\na - Gestionar juegos.\nb - Mostar informes.\n0 - Salir.")
        opcion = input("Introduce la tarea que quieras realizar: ")
        
        match opcion:
            case "a":
                while True:
                    print("\n1 - Dar de alta un juego.\n2 - Editar un juego.\n3 - Eliminar un juego.\n0 - Volver.")
                    opcion = input("Introduce una opción: ")
                    
                    match opcion:
                        case "1":
                            print()
                            break

                        case "2":
                            print()
                            break
                        
                        case "3":
                            print()
                            break

                        case "0":
                            break
                        
                        case _:
                            print("No has introducido una opción correcta.")
            
            case "b":
                while True:
                    print("\n1 - Listar todos los juegos.\n2 - Listar todos los editores.\n3 - Listar todos los juegos por genero.\n4 - Listar todos los juegos del siglo XX.\n5 - Listar todos los juegos publicados en años pares.\n6 - Listar todos los juego de Nintendo.\n7 - Listar todos los juegos con mayor media de ventas.\n8 - Listar los 5 juegos mas vendidos de NA, Europa, Japón y del resto del mundo.\n0 - Salir.")
                    opcion = input("Introduce una opción: ")
                    
                    match opcion:
                        case "1":
                            print(Listado.listado_juegos())
                            break

                        case "2":
                            print()
                            break
                        
                        case "3":
                            print()
                            break

                        case "4":
                            print()
                            break

                        case "5":
                            print()
                            break
                        
                        case "6":
                            print()
                            break
                        
                        case "7":
                            print()
                            break
                        
                        case "8":
                            print()
                            break
                        
                        case "0":
                            break

                        case _:
                            print("No has introducido una opcion correcta.")

            case "0":
                break

            case _:
                print("No has elegido una opcion correcta.")

menu()