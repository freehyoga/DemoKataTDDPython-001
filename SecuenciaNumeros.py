__author__ = 'af.carrion, se.perezf'

class SecuenciaNumeros:

    def longitud(self,cadena):
        if cadena == "":
            return 0
        elif "," in cadena:
            return len(cadena.split(","))
        else:
            return int(cadena)

    def minimo(self, cadena):
        pass
