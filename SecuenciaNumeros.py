__author__ = 'af.carrion, se.perezf'

class SecuenciaNumeros:

    def a_arreglo(self, cadena):
        #funtion map: es "equivalente" a for x in cadena
        return map(float, cadena.split(","))

    def longitud(self,cadena):
        if cadena == "":
            return 0
        return len(self.a_arreglo(cadena))

    def minimo(self, cadena):
        if cadena == "":
            return 0
        return min(self.a_arreglo(cadena))

    def maximo(self,cadena):
        if cadena == "":
            return 0
        return max(self.a_arreglo(cadena))

    def promedio(self, cadena):
        if cadena == "":
            return 0
        promedio_arreglo = self.a_arreglo(cadena)
        return sum(promedio_arreglo)/len(promedio_arreglo)

    def analizar(self, cadena):
        return [self.longitud(cadena), self.minimo(cadena), self.maximo(cadena), self.promedio(cadena)]