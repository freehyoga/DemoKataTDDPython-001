from unittest import TestCase

__author__ = 'af.carrion, se.perezf'

from SecuenciaNumeros import SecuenciaNumeros

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


