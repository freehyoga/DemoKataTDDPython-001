from unittest import TestCase
from SecuenciaNumeros import SecuenciaNumeros

__author__ = 'af.carrion, se.perezf'

class TestSecuenciaNumeros(TestCase):

    #Longitud
    def test_longitud(self):
        self.assertEqual(SecuenciaNumeros().longitud(""),0,"Cadena Vacia")

    def test_longitud_uno(self):
        self.assertEqual(SecuenciaNumeros().longitud("1"),1,"Un numero")

    def test_longitud_dos(self):
        self.assertEqual(SecuenciaNumeros().longitud("1,2"),2, "Dos Numeros")

    def test_longitud_n(self):
        self.assertEqual(SecuenciaNumeros().longitud("1,5,3,8"),4, "Cuatro Numeros.")

    #Minimo
    def test_minimo_vacio(self):
        self.assertEqual(SecuenciaNumeros().minimo(""),0,"Minimo de una cadena vacia")

    def test_minimo_uno(self):
        self.assertEqual(SecuenciaNumeros().minimo("7"),7, "Minimo de un numero")

    def test_minimo_dos(self):
        self.assertEqual(SecuenciaNumeros().minimo("12,2"), 2, "Minimo de dos numeros")

    def test_minimo_n(self):
        self.assertEqual(SecuenciaNumeros().minimo("10,5,128,3,12"), 3, "Minimo de tres numeros.")

    #Maximo
    def test_maximo_vacio(self):
        self.assertEqual(SecuenciaNumeros().maximo(""), 0, "Maximo de una cadena vacia")

    def test_maximo_uno(self):
        self.assertEqual(SecuenciaNumeros().maximo("7"), 7, "Maximo de un numero")

    def test_maximo_dos(self):
        self.assertEqual(SecuenciaNumeros().maximo("1,2"), 2, "Maximo de dos numeros")

    def test_maximo_n(self):
        self.assertEqual(SecuenciaNumeros().maximo("1,2,3,24,4,24,4,354,24,5"), 354, "Maximo n numeros")

    #Promedio
    def test_promedio_vacio(self):
        self.assertEqual(SecuenciaNumeros().promedio(""), 0, "Promedio Cadena Vacia")


