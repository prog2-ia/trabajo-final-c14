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

# CLASE BIBLIOTECA
class Biblioteca:
    def _init_(self):
        self.pistas = []
        self.playlists = []

    def agregar_pista(self, pista):
        self.pistas.append(pista)

    def crear_playlist(self, playlist):
        self.playlists.append(playlist)

    def buscar_por_genero(self, genero):
        resultado = []
        for p in self.pistas:
            if p.genero == genero:
                resultado.append(p)
        return resultado

# DEMO
if _name_ == "_main_":
    p1 = Pista("Numb", "Linkin Park", "rock", 185)
    p2 = Pista("Blinding Lights", "The Weeknd", "pop", 200)
    p3 = Pista("Viva la Vida", "Coldplay", "pop", 240)

    print("Duración válida:", Pista.duracion_valida(200))

    biblio = Biblioteca()
    biblio.agregar_pista(p1)
    biblio.agregar_pista(p2)
    biblio.agregar_pista(p3)

    lista = Playlist("Viaje", "feliz")
    lista.agregar_pista(p2)
    lista.agregar_pista(p3)

    biblio.crear_playlist(lista)

    lista.mostrar()

    print("Total pistas creadas:", Pista.cantidad_pistas())