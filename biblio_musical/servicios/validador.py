class Validador:
    """
    Centraliza la lógica de validación de metadatos musicales.
    """

    @staticmethod
    def duracion_valida(duracion: float) -> bool:
        """Verifica que la duración sea un número positivo mayor a cero."""
        return duracion > 0

    @staticmethod
    def titulo_valido(titulo: str) -> bool:
        """ Valida que el título sea una cadena de texto no vacía y que no contenga solo espacios en blanco."""
        return isinstance(titulo, str) and len(titulo.strip()) > 0

    @staticmethod
    def artista_valido(artista: str) -> bool:
        """ Comprueba que el nombre del artista sea una cadena válida """
        return isinstance(artista, str) and len(artista.strip()) > 0

    @staticmethod
    def genero_valido(genero: str) -> bool:
        """ Acepta cualquier género no vacío. """
        return isinstance(genero, str) and len(genero.strip()) > 0