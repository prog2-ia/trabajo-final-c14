# María Mestre Sánchez y Sandra Crevillen Contreras
# Proyecto Programación 2 - Biblioteca musical y playlists (VERSIÓN BÁSICA)

# CLASE PISTA 
class Pista:
    total_pistas = 0  # atributo de clase

    def __init__(self, titulo, artista, genero, duracion):
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.duracion = duracion  # segundos
        Pista.total_pistas += 1

    def info(self):
        return f"{self.artista} - {self.titulo} ({self.genero}) [{self.duracion}s]"

    @classmethod
    def cantidad_pistas(cls):
        return cls.total_pistas

    @staticmethod
    def duracion_valida(duracion):
        return duracion > 0

# CLASE PLAYLIST 
class Playlist:
    def __init__(self, nombre, estado_animo):
        self.nombre = nombre
        self.estado_animo = estado_animo
        self.pistas = []

    def agregar_pista(self, pista):
        self.pistas.append(pista)

    def duracion_total(self):
        total = 0
        for p in self.pistas:
            total += p.duracion
        return total

    def mostrar(self):
        print(f"Playlist: {self.nombre} ({self.estado_animo})")
        for p in self.pistas:
            print(p.info())
        print(f"Duración total: {self.duracion_total()}s")