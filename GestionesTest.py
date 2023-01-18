import unittest

import Gestiones

class TestUtils(unittest.TestCase):
    def test_alta_juego(self):
        self.assertEqual(Gestiones.alta_juegos(), "16601")

if __name__ == "__main__":
    unittest.main()