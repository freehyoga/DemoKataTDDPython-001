from unittest import TestCase

__author__ = 'af.carrion'

from SecuenciaNumeros import SecuenciaNumeros

class TestSecuenciaNumeros(TestCase):

    def test_longitud(self):
        self.assertEqual(SecuenciaNumeros().longitud(""),0,"Cadena Vacia")

    def test_longitud_uno(self):
        self.assertEqual(SecuenciaNumeros().longitud("1"),1,"Un numero")