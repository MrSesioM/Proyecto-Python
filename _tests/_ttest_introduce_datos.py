import unittest, Gestiones, random

variable = input(int("\nSe generaran 11 valores en una lista (numero o texto dependiendo de la posicion en la lista), indica cuantas listas quieres comprobar en la funcion Introduce_datos()"))
letras = "abcdefghijklmnopqrstuvwxyz" 
letra_aleatoria = random.choice(letras) + random.choice(letras) + random.choice(letras) + random.choice(letras) + random.choice(letras) + random.choice(letras)
lista = []

class Test_Utils(unittest.TestCase):

    def test_introduce_datos(self):
    
        for contador in range(variable):  
            for i in range(11):
                lista.append()
                if i==4:
                    lista.append(random.randint(1900,2050))
                elif i>=7:
                    lista.append(random.randint(0,10))
            print(f"{contador}.Probando lista --> {lista}")         
            self.assertEquals(Gestiones.introduce_datos(), lista)


if __name__ == '__main__':
    unittest.main()