from pista import Pista
from playlist import Playlist
from playlist_publica import PlaylistPublica
from playlist_privada import PlaylistPrivada
from playlist_compartida import PlaylistCompartida
from biblioteca import Biblioteca
from reproductor import Reproductor
from estadistica import Estadistica
from genero import Genero
from artista import Artista
from album import Album
from usuario import Usuario
from usuario_gratis import UsuarioGratis
from usuario_premium import UsuarioPremium
from usuario_administrador import UsuarioAdministrador
from usuario_super import UsuarioSuper
from validador import Validador

if __name__ == "__main__":
    print("==== PRUEBA DEL CÓDIGO ===\n")

    # Crear géneros
    rock = Genero("Rock")
    pop = Genero("Pop")

    # Crear pistas
    p1 = Pista("Blinding Lights", "The Weeknd", rock, 185)
    p2 = Pista("Levitating", "Dua Lipa", pop, 240)
    p3 = Pista("Good 4 U", "Olivia Rodrigo", pop, 355)

    print("Pistas creadas:")
    print(p1)
    print(p2)
    print(p3)
    print(f"Total pistas: {Pista.total_pistas}\n")

    # Marcar favorita
    p1.marcar_favorita()
    print(f"{p1.titulo} es favorita: {p1.is_favorita()}\n")

    # Crear artista
    artista1 = Artista("The Weeknd")
    album1 = Album("After Hours", artista1, 2020)
    artista1.agregar_album(album1)
    print(f"Artista: {artista1.nombre}")
    artista1.mostrar_albums()
    print()

    # Crear playlists
    playlist_normal = Playlist("Viaje", "feliz")
    playlist_normal.agregar_pista(p1)
    playlist_normal.agregar_pista(p2)

    playlist_publica = PlaylistPublica("Fiesta", "energico")
    playlist_publica.agregar_pista(p2)
    playlist_publica.agregar_pista(p3)

    usuario1 = Usuario("Juan", "juan@email.com", 25, "Madrid")
    playlist_privada = PlaylistPrivada("Privada", "tranquilo", usuario1)
    playlist_privada.agregar_pista(p1)

    playlist_compartida = PlaylistCompartida("Compartida", "divertido")
    playlist_compartida.agregar_colaborador(usuario1)
    playlist_compartida.agregar_pista(p3, usuario1)

    print("Playlists creadas:")
    print(playlist_normal)
    print(playlist_publica)
    print(playlist_privada)
    print(playlist_compartida)
    print()

    # Mostrar playlists
    print("Contenido de playlist normal:")
    playlist_normal.mostrar_playlist()
    print()

    print("Contenido de playlist pública:")
    playlist_publica.mostrar_playlist()
    print()

    print("Contenido de playlist privada (usuario correcto):")
    playlist_privada.mostrar_playlist(usuario1)
    print()

    # Usuarios
    usuario_gratis = UsuarioGratis("Ana", "ana@email.com", 22, "Barcelona")
    usuario_premium = UsuarioPremium("Carlos", "carlos@email.com", 30, "Valencia")
    usuario_admin = UsuarioAdministrador("Admin", "admin@email.com", 35, "Sevilla")
    usuario_super = UsuarioSuper("SuperUser", "super@email.com", 28, "Bilbao")

    print("Usuarios creados:")
    print(usuario_gratis)
    print(usuario_premium)
    print(usuario_admin)
    print(usuario_super)
    print()

    # Crear playlists para usuarios
    usuario_gratis.crear_playlist(playlist_normal)
    usuario_premium.crear_playlist(playlist_publica)
    usuario_admin.crear_playlist(playlist_privada)

    print("Playlists de usuario gratis:")
    usuario_gratis.mostrar_playlists()
    print()

    # Buscar playlist
    encontrada = usuario_gratis.buscar_playlist("Viaje")
    if encontrada:
        print(f"Playlist encontrada: {encontrada}")
    else:
        print("Playlist no encontrada")
    print()

    # Funciones de premium y admin
    usuario_premium.descargar_playlist(playlist_publica)
    usuario_admin.eliminar_playlist(usuario_gratis, playlist_normal)
    print()

    # Usuario super
    usuario_super.gestionar_y_descargar(usuario_premium, playlist_publica)
    print()

    # Reproductor
    repro = Reproductor()
    print("Reproduciendo pista:")
    repro.reproducir(p1)
    print()

    # Estadísticas
    pistas = [p1, p2, p3]
    mas_larga = Estadistica.pista_mas_larga(pistas)
    print(f"Pista más larga: {mas_larga.info()}")
    print()

    # Validador
    print("Validaciones:")
    print(f"Duración válida (185): {Validador.duracion_valida(185)}")
    print(f"Título válido ('Numb'): {Validador.titulo_valido('Numb')}")
    print(f"Género válido ('Rock'): {Validador.genero_valido('Rock')}")
    print(f"Género válido ('Unknown'): {Validador.genero_valido('Unknown')}")
    print()

    print("=== Fin de la prueba ===")