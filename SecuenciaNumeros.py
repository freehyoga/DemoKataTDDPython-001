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
        if cadena == "":
            return 0
        elif "," in cadena:
            #funtion map: es equivalente a for x in cadena
            minimo = map(int, cadena.split(","))
            #function min It returns the smallest item in an iterable or the smallest of two or more arguments.
            return min(minimo)
        else:
            return int(cadena)

    def maximo(self,cadena):
        if cadena == "":
            return 0
        elif "," in cadena:
            maximo_arreglo = map(int, cadena.split(","))
            return max(maximo_arreglo)
        else:
            return int(cadena)

    def promedio(self, cadena):
        return