from unittest import TestCase

__author__ = 'af.carrion, se.perezf'

from SecuenciaNumeros import SecuenciaNumeros

class TestSecuenciaNumeros(TestCase):

    def test_longitud(self):
        self.assertEqual(SecuenciaNumeros().longitud(""),0,"Cadena Vacia")

    def test_longitud_uno(self):
        self.assertEqual(SecuenciaNumeros().longitud("1"),1,"Un numero")

    def test_longitud_dos(self):
        self.assertEqual(SecuenciaNumeros().longitud("1,2"),2, "Dos Numeros")

    def test_longitud_n(self):
        self.assertEqual(SecuenciaNumeros().longitud("1,5,3,8"),4, "Cuatro Numeros.")