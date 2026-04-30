from biblio_musical.contenido.elemento_musical import ElementoMusical

class Pista(ElementoMusical):
    """Representa una pista musical."""
    total_pistas = 0
    def __init__(self, titulo, artista, genero, duracion, favorita=False):
        super().__init__(titulo, artista, genero, duracion)
        self._favorita = favorita
        Pista.total_pistas += 1

    @property
    def favorita(self):
        return self._favorita

    @favorita.setter
    def favorita(self, value):
        self._favorita = value

    def is_favorita(self):
        return self._favorita

    def marcar_favorita(self):
        """Marca la pista como favorita."""
        self._favorita = True

    def quitar_favorita(self):
        """Quita la pista de favoritas."""
        self._favorita = False

    def reproducir(self):
        """Reproduce."""
        print(f" Reproduciendo: {self.titulo} - {self.artista}")

    @classmethod
    def cantidad_pistas(cls):
        return cls.total_pistas

    def __str__(self):
        return f"Pista: {self.titulo} - {self.artista} ({self.duracion}s)"

    def __repr__(self):
        return f"Pista('{self.titulo}', '{self.artista}', '{self.genero}', {self.duracion})"