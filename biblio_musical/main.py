from biblio_musical.contenido.pista import Pista
from playlist import Playlist
from biblio_musical.servicios.biblioteca import Biblioteca
from biblio_musical.contenido.genero import Genero
from biblio_musical.servicios.validador import Validador

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
    print("\n=== MENÚ ===")
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


def agregar_pista_a_playlist(biblioteca):
    if not biblioteca._pistas:
        print("No hay pistas en la biblioteca para agregar.")
        return
    if not biblioteca._playlists:
        print("No hay playlists en la biblioteca.")
        return

    listar_pistas(biblioteca)
    indice_pista = input("Selecciona el número de la pista: ").strip()
    listar_playlists(biblioteca)
    indice_playlist = input("Selecciona el número de la playlist: ").strip()

    try:
        pista = biblioteca._pistas[int(indice_pista) - 1]
        playlist = biblioteca._playlists[int(indice_playlist) - 1]
    except (ValueError, IndexError):
        print("Selección incorrecta. Intenta de nuevo.")
        return

    playlist.agregar_pista(pista)
    print(f"Pista '{pista.titulo}' añadida a '{playlist.titulo}'.")


def buscar_pistas(biblioteca):
    criterio = input("Buscar por título, artista o género: ").strip().lower()
    if not criterio:
        print("Debes escribir algo para buscar.")
        return

    resultados = [p for p in biblioteca._pistas
                  if criterio in p.titulo.lower()
                  or criterio in p.artista.lower()
                  or criterio in str(p.genero).lower()]

    if not resultados:
        print("No se han encontraron pistas con ese criterio.")
        return

    print("Resultados de tu búsqueda:")
    for pista in resultados:
        print(pista)


def reproducir_pista(biblioteca):
    if not biblioteca._pistas:
        print("No hay pistas en la biblioteca.")
        return
    listar_pistas(biblioteca)
    opcion = input("Selecciona el número de la pista que quieres reproducir: ").strip()
    try:
        pista = biblioteca._pistas[int(opcion) - 1]
        pista.reproducir()
    except (ValueError, IndexError):
        print("Selección inválida.")


def reproducir_playlist(biblioteca):
    if not biblioteca._playlists:
        print("No hay playlists en la biblioteca.")
        return
    listar_playlists(biblioteca)
    opcion = input("Selecciona el número de la playlist que quieres reproducir: ").strip()
    try:
        playlist = biblioteca._playlists[int(opcion) - 1]
        playlist.reproducir()
    except (ValueError, IndexError):
        print("Selección inválida.")


def mostrar_estadisticas(biblioteca):
    total_pistas = len(biblioteca._pistas)
    total_playlists = len(biblioteca._playlists)
    duracion_total = sum(p.duracion for p in biblioteca._pistas)
    print("\nEstadísticas:")
    print(f"- Pistas: {total_pistas}")
    print(f"- Playlists: {total_playlists}")
    print(f"- Duración total de todas las pistas: {duracion_total} segundos")


def main():
    biblioteca = Biblioteca()
    crear_datos_ejemplo(biblioteca)

    print("\nBienvenido a la Biblioteca Musical.")

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            listar_pistas(biblioteca)
        elif opcion == "2":
            listar_playlists(biblioteca)
        elif opcion == "3":
            crear_pista_interactiva(biblioteca)
        elif opcion == "4":
            crear_playlist_interactiva(biblioteca)
        elif opcion == "5":
            agregar_pista_a_playlist(biblioteca)
        elif opcion == "6":
            buscar_pistas(biblioteca)
        elif opcion == "7":
            reproducir_pista(biblioteca)
        elif opcion == "8":
            reproducir_playlist(biblioteca)
        elif opcion == "9":
            mostrar_estadisticas(biblioteca)
        elif opcion == "0":
            print("Gracias por usar la Biblioteca Musical")
            break
        else:
            print("Esta opción no ves álida. Elige del 0 al 9.")


if __name__ == "__main__":
    main()