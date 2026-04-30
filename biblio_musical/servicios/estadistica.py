"""  Esta clase ofrece métodos estáticos para analizar listas de pistas musicales """
class Estadistica:

    @staticmethod
    def pista_mas_larga(lista_pistas):
        """ Devuelve la pista con mayor duración de la lista """
        mayor = lista_pistas[0]
        for p in lista_pistas:
            if p.duracion > mayor.duracion:
                mayor = p
        return mayor

    @staticmethod
    def pista_mas_corta(lista_pistas):
        """ Devuelve la pista con menor duración de la lista """
        menor = lista_pistas[0]
        for p in lista_pistas:
            if p.duracion < menor.duracion:
                menor = p
        return menor

    @staticmethod
    def duracion_total(lista_pistas):
        """ Calcula la duración total sumando todas las pistas """
        total = 0
        for p in lista_pistas:
            total += p.duracion
        return total

    @staticmethod
    def promedio_duracion(lista_pistas):
        """ Calcula el promedio de duración de las pistas """
        total = Estadistica.duracion_total(lista_pistas)
        return total / len(lista_pistas)  # Duración total / número de pistas