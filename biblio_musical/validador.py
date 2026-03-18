class Validador:
    @staticmethod
    def duracion_valida(duracion):
        return duracion > 0

    @staticmethod
    def titulo_valido(titulo):
        return isinstance(titulo, str) and len(titulo.strip()) > 0

    @staticmethod
    def artista_valido(artista):
        return isinstance(artista, str) and len(artista.strip()) > 0

    @staticmethod
    def genero_valido(genero):
        generos_validos = ["Rock", "Pop", "Jazz", "Clásica", "Electrónica", "Hip-Hop", "Reggae", "Blues"]
        return genero in generos_validos