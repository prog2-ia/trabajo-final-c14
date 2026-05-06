from contenido.coleccion_musical import ColeccionMusical

class Album(ColeccionMusical):
    """Representa un álbum musical que contiene múltiples pistas."""

    def __init__(self, titulo, artista, año):
        super().__init__(titulo)
        self._artista = artista
        self.año = año

    def mostrar_album(self):
        """Muestra la información resumida del álbum."""
        duracion = self.obtener_duracion_total()
        print(f"Album: {self.titulo} ({self.año}) - {self._artista.nombre}")
        print(f"Duracion total: {duracion}")
        print("-" * 30)
        
        if not self._pistas:
            print("El album no tiene pistas registradas.")
        else:
            for i, p in enumerate(self._pistas, 1):
                print(f"{i}. {p.info()}")

    def obtener_duracion_total(self):
        """Calcula la duracion en formato MM:SS."""
        total_segundos = sum(p.duracion for p in self._pistas)
        minutos = total_segundos // 60
        segundos = total_segundos % 60
        return f"{minutos}:{segundos:02d}"

    def reproducir(self):
        """Reproduce todas las pistas del álbum (polimorfismo)."""
        print(f"Reproduciendo album: {self.titulo}")
        for pista in self._pistas:
            pista.reproducir()

    def __str__(self):
        return f"Album: {self.titulo} - {self._artista.nombre} ({len(self._pistas)} pistas)"

    def __repr__(self):
        return f"{self.__class__.__name__}(titulo='{self.titulo}', artista='{self._artista.nombre}', pistas={len(self._pistas)})"
    
    def __lt__(self, otro):
        """Ordena albumes por año."""
        if not isinstance(otro, Album):
            return NotImplemented
        return self.año < otro.año

    def __eq__(self, otro):
        """Comprueba si dos albumes son iguales por titulo y artista."""
        if not isinstance(otro, Album):
            return False
        return self.titulo == otro.titulo and self._artista == otro._artista