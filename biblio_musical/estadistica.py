class Estadistica:
   
    @staticmethod
    def pista_mas_larga(lista_pistas):
        mayor = lista_pistas[0]
        for p in lista_pistas:
            if p.duracion > mayor.duracion:
                mayor = p
        return mayor


    @staticmethod
    def pista_mas_corta(lista_pistas):
        menor = lista_pistas[0]
        for p in lista_pistas:
            if p.duracion < menor.duracion:
                menor = p
        return menor


    @staticmethod
    def duracion_total(lista_pistas):
        total = 0
        for p in lista_pistas:
            total += p.duracion
        return total


    @staticmethod
    def promedio_duracion(lista_pistas):
        total = Estadistica.duracion_total(lista_pistas)
        return total / len(lista_pistas)