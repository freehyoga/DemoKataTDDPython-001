from unittest import TestCase

__author__ = 'af.carrion'

import SecuenciaNumeros

class TestSecuenciaNumeros(TestCase):

    def test_longitud(self):
        self.assertEqual(SecuenciaNumeros().longitud(""),0,"Cadena Vacia")
