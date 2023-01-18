import unittest, Gestiones

class TestUtils(unittest.TestCase):
    def test_alta_juego(self):
        self.assertEqual(Gestiones.alta_juegos(), [16601, 'test', 'test', 2000, 'test', 'test', 20.0, 20.0, 20.0, 20.0, 20.0])
        self.assertEqual(Gestiones.alta_juegos(), [16602, 'test2', 'test2', 2000, 'test2', 'test2', 20.0, 20.0, 20.0, 20.0, 20.0])

if __name__ == "__main__":
    unittest.main()