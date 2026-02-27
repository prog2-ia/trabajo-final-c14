class Estadistica:
    @staticmethod
    def pista_mas_larga(lista_pistas):
        mayor = lista_pistas[0]
        for p in lista_pistas:
            if p.duracion > mayor.duracion:
                mayor = p
        return mayor