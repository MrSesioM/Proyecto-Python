import unittest,random,Gestiones

variable = input("\nSe generaran 11 valores aleatorios para una lista (numero o texto dependiendo de la posicion en la lista de los juegos).\nLa funcion compara el tipo cada elemento de la lista generada contra la lista que contiene los detalles de un juego.\nIndica el nº de listas para comprobar en la funcion Introduce_datos().\n\n>")
letras = "abcdefghijklmnopqrstuvwxyz"

class Test_Utils(unittest.TestCase):

    def test_introduce_datos(self):
        
      
        for contador in range(int(variable)):
            
            lista = []
            lista_juego = []
            letras = "abcdefghijklmnopqrstuvwxyz"
            
            for i in range(11):

                if (i == 0 or i==3): 
                    lista.append(random.randint(0, 2050))
                    lista_juego.append(int(Gestiones.lista[contador][i]))
                elif (i >= 6):
                    lista.append(float(random.randint(0, 2050)))
                    lista_juego.append(float(Gestiones.lista[contador][i]))
                else:
                    lista.append(random.choice(letras) + random.choice(letras) + random.choice(
                        letras) + random.choice(letras) + random.choice(letras) + random.choice(letras))
                    lista_juego.append(Gestiones.lista[contador][i])

            print("Probando lista Nº:", contador, "-->", lista,"-->",lista_juego)

            self.assertTrue(type(lista_juego),type(lista))
            

if __name__ == '__main__':
    unittest.main()
