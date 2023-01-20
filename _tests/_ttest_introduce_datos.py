import unittest, Gestiones, random

variable = input("\nSe generaran 11 valores en una lista (numero o texto dependiendo de la posicion en la lista), indica cuantas listas quieres comprobar en la funcion Introduce_datos()\n\n>")
letras = "abcdefghijklmnopqrstuvwxyz" 
lista = []
lista_juego=[]

class Test_Utils(unittest.TestCase):

    def test_introduce_datos(self):
    
        for contador in range(int(variable)):  
            for i in range(11):
                
                if (i==0 or i==3 or i>=6):
                    lista.append(random.randint(1900,2050))
                    lista_juego.append(Gestiones.lista[contador][i])
                else:
                    lista.append(random.choice(letras) + random.choice(letras) + random.choice(letras) + random.choice(letras) + random.choice(letras) + random.choice(letras))
                    lista_juego.append(Gestiones.lista[contador][i])
            
                    print("Probando lista Nº:",contador,"-->" ,lista)         
            
            self.assertEqual(lista_juego, lista)


if __name__ == '__main__':
    unittest.main()