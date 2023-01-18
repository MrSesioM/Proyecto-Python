import unittest, Gestiones

class PruebaIntroduceDatos(unittest.TestCase):
    def test_introduce_datos(self):
        self.assertEqual(Gestiones.introduce_datos(), ['rank', 'Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales'])

if __name__ == '__main__':
    unittest.main()