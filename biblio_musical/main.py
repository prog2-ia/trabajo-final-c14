from pista import Pista
from playlist import Playlist
from biblioteca import Biblioteca
from genero import Genero
from validador import Validador

genero_referencias = [
    "Rock",
    "Pop",
    "Jazz",
    "Clásica",
    "Electrónica",
    "Hip-Hop",
    "Reggae",
    "Blues",
]


def crear_datos_ejemplo(biblioteca):
    rock = Genero("Rock")
    pop = Genero("Pop")
    jazz = Genero("Jazz")

    p1 = Pista("Blinding Lights", "The Weeknd", rock, 185)
    p2 = Pista("Levitating", "Dua Lipa", pop, 240)
    p3 = Pista("Good 4 U", "Olivia Rodrigo", pop, 200)
    p4 = Pista("Take Five", "Dave Brubeck", jazz, 330)

    biblioteca.agregar_pista(p1)
    biblioteca.agregar_pista(p2)
    biblioteca.agregar_pista(p3)
    biblioteca.agregar_pista(p4)

    playlist1 = Playlist("Viaje", "Feliz")
    playlist1.agregar_pista(p1)
    playlist1.agregar_pista(p2)
    biblioteca.crear_playlist(playlist1)

    playlist2 = Playlist("Descanso", "Relajado")
    playlist2.agregar_pista(p3)
    playlist2.agregar_pista(p4)
    biblioteca.crear_playlist(playlist2)

    return biblioteca


def mostrar_menu():
    print("\n=== MENÚ - BIBLIOTECA MUSICAL ===")
    print("1. Ver todas las pistas")
    print("2. Ver todas las playlists")
    print("3. Crear nueva pista")
    print("4. Crear nueva playlist")
    print("5. Agregar pista a playlist")
    print("6. Buscar pistas")
    print("7. Reproducir pista")
    print("8. Reproducir playlist")
    print("9. Estadísticas básicas")
    print("0. Salir")


def pedir_genero():
    print("Géneros disponibles:")
    for genero in genero_referencias:
        print(f" - {genero}")

    while True:
        texto = input("Introduce un género: ").strip().title()
        if Validador.genero_valido(texto):
            return Genero(texto)
        print("Género no válido. Prueba otro de la lista.")


def pedir_duracion():
    while True:
        valor = input("Introduce la duración en segundos: ").strip()
        if not valor.isdigit():
            print("Introduce un número entero positivo.")
            continue
        duracion = int(valor)
        if Validador.duracion_valida(duracion):
            return duracion
        print("La duración debe ser mayor que 0.")


def listar_pistas(biblioteca):
    if not biblioteca._pistas:
        print("No hay pistas en la biblioteca.")
        return
    print("\nPistas disponibles:")
    for idx, pista in enumerate(biblioteca._pistas, start=1):
        print(f"{idx}. {pista}")


def listar_playlists(biblioteca):
    if not biblioteca._playlists:
        print("No hay playlists en la biblioteca.")
        return
    print("\nPlaylists disponibles:")
    for idx, playlist in enumerate(biblioteca._playlists, start=1):
        print(f"{idx}. {playlist}")


def buscar_pista_por_titulo(biblioteca, titulo):
    titulo = titulo.strip().lower()
    for pista in biblioteca._pistas:
        if pista.titulo.strip().lower() == titulo:
            return pista
    return None


def crear_pista_interactiva(biblioteca):
    titulo = input("Título de la pista: ").strip()
    artista = input("Artista: ").strip()
    genero = pedir_genero()
    duracion = pedir_duracion()

    if not Validador.titulo_valido(titulo):
        print("Título inválido. No se ha creado la pista.")
        return
    if not Validador.artista_valido(artista):
        print("Artista inválido. No se ha creado la pista.")
        return

    nueva_pista = Pista(titulo, artista, genero, duracion)
    biblioteca.agregar_pista(nueva_pista)
    print(f"Pista creada: {nueva_pista}")


def crear_playlist_interactiva(biblioteca):
    nombre = input("Nombre de la playlist: ").strip()
    estado = input("Estado de ánimo de la playlist: ").strip()
    if not nombre:
        print("El nombre de la playlist no puede estar vacío.")
        return

    nueva_playlist = Playlist(nombre, estado)
    biblioteca.crear_playlist(nueva_playlist)
    print(f"Playlist creada: {nueva_playlist}")