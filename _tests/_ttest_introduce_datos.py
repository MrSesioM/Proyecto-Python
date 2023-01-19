import unittest, Gestiones, random

variable = input("\nSe generaran 11 valores en una lista (numero o texto dependiendo de la posicion en la lista), indica cuantas listas quieres comprobar en la funcion Introduce_datos()\n\n>")
letras = "abcdefghijklmnopqrstuvwxyz" 
palabra = random.choice(letras) + random.choice(letras) + random.choice(letras) + random.choice(letras) + random.choice(letras) + random.choice(letras)
lista = []

class Test_Utils(unittest.TestCase):

    def test_introduce_datos(self):
    
        for contador in range(int(variable)):  
            for i in range(11):
                
                if i==1 or i==3 or i==5 or i==6:
                    lista.append(random.choice(letras) + random.choice(letras) + random.choice(letras) + random.choice(letras) + random.choice(letras) + random.choice(letras))
                if i==0:
                    lista.append(int(random.randint(1900,2050)))
                elif i==4:
                    lista.append(int(random.randint(1900,2050)))
                    lista.append(int(random.randint(1900,2050)))
                elif i>=7:
                    lista.append(random.randint(0,10))

            print("Probando lista -->" ,lista)         
            
            self.assertEqual(Gestiones.lista[contador], lista)


if __name__ == '__main__':
    unittest.main()