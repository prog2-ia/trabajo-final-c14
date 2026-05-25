"""
Módulo Principal de Interfaz de Usuario

Coordina el flujo completo de la biblioteca musical, gestionando el inicio de sesión,
los formularios de entrada de datos, el enrutamiento de menús según el tipo de cuenta 
y la persistencia final de la sesión.
"""

import os
from contenido.pista import Pista
from contenido.genero import Genero
from playlist.playlist import Playlist
from servicios.biblioteca import Biblioteca
from servicios.gestor_usuarios import GestorUsuarios, TIPOS_USUARIO
from usuarios.usuario_premium import UsuarioPremium
from usuarios.usuario_administrador import UsuarioAdministrador
from usuarios.usuario_super import UsuarioSuper

#rutas globales del sistema
CARPETA_DATOS = os.path.abspath(os.path.join(os.path.dirname(__file__), "datos"))

GENEROS_DISPONIBLES = [
    "Rock", "Pop", "Jazz", "Clásica", "Electrónica",
    "Hip-Hop", "Reggae", "Blues", "Reggaeton", "Trap", "Indie",
]

# datos de ejemplos
def crear_datos_ejemplo(biblioteca):
    """
    Puebla la biblioteca global con un conjunto inicial de géneros, pistas y playlists
    de demostración
    
    Args:
        biblioteca: Instancia global de la biblioteca a rellenar.
    """
    rock = Genero("Rock") 
    pop = Genero("Pop")
    jazz = Genero("Jazz")
    reggaeton = Genero("Reggaeton")
    indie = Genero("Indie")

    p1 = Pista("Blinding Lights","The Weeknd",rock,185)
    p2 = Pista("Levitating","Dua Lipa",pop,240)
    p3 = Pista("Good 4 U","Olivia Rodrigo",pop,200)
    p4 = Pista("Take Five","Dave Brubeck",jazz,330)
    p5 = Pista("Espresso","Sabrina Carpenter",pop,175)
    p6 = Pista("Gata Only","FloyyMenor x Cris Mj", reggaeton, 222)
    p7 = Pista("LUNCH","Billie Eilish",indie,180)
    p8 = Pista("Si Antes Te Hubiera Conocido", "Karol G", reggaeton, 195)
    p9 = Pista("Houdini", "Dua Lipa",pop,185)

    for p in [p1, p2, p3, p4, p5, p6, p7, p8, p9]:
        biblioteca.agregar_pista(p)

    pl1 = Playlist("Viaje", "Feliz")
    pl1.agregar_pista(p1); pl1.agregar_pista(p2)
    pl1.agregar_pista(p5); pl1.agregar_pista(p9)

    pl2 = Playlist("Descanso", "Relajado")
    pl2.agregar_pista(p3); pl2.agregar_pista(p4)

    pl3 = Playlist("Fiesta", "Motivado")
    pl3.agregar_pista(p3); pl3.agregar_pista(p6); pl3.agregar_pista(p8)

    biblioteca.crear_playlist(pl1)
    biblioteca.crear_playlist(pl2)
    biblioteca.crear_playlist(pl3)


def crear_usuarios_ejemplo(gestor):
    """
    Registra un conjunto inicial de usuarios con diferentes perfiles y roles
    
    Args:
        gestor: El gestor de usuarios encargado de procesar el alta y almacenamiento.
    """
    gestor.agregar(gestor.crear_usuario("Ana",    "ana@gmail.com",   20, "Madrid",    "gratis"))
    gestor.agregar(gestor.crear_usuario("Luis",   "luis@gmail.com",  25, "Barcelona", "premium"))
    gestor.agregar(gestor.crear_usuario("Carlos", "admin@gmail.com", 30, "Valencia",  "administrador"))
    gestor.agregar(gestor.crear_usuario("Sergio", "super@gmail.com", 35, "Sevilla",   "super"))
    gestor.guardar()
    gestor.guardar_pickle()
    print("Usuarios de ejemplo creados.")

# funciones de entrada
def pedir_genero():
    """
    Muestra la lista de géneros disponibles y solicita al usuario seleccionar o 
    introducir un nuevo género por teclado, garantizando su validez.
    
    Returns:
        Un objeto Genero inicializado con la cadena introducida.
    """
    print("Géneros disponibles:")
    for g in GENEROS_DISPONIBLES:
        print(f"  - {g}")
    while True:
        texto = input("Género: ").strip().title()
        if not texto:
            print("No puede estar vacío.")
            continue
        if texto not in GENEROS_DISPONIBLES:
            GENEROS_DISPONIBLES.append(texto)
            print(f"Género '{texto}' añadido.")
        return Genero(texto)


def pedir_duracion():
    """
    Solicita una duración temporal por consola controlando que el formato ingresado se corresponda con un entero positivo.
    
    Returns:
        El número de segundos como entero.
    """
    while True:
        try:
            d = int(input("Duración en segundos: ").strip())
            if d > 0:
                return d
            print("Debe ser mayor que 0.")
        except ValueError:
            print("Introduce un número entero.")


def pedir_indice(lista, mensaje):
    """Pide un número por consola y devuelve el elemento de la lista, o None."""
    try:
        return lista[int(input(mensaje).strip()) - 1]
    except (ValueError, IndexError):
        print("Selección inválida.")
        return None

# pantalla de login
def pantalla_login(gestor):
    """Muestra el menú de login y devuelve el usuario activo, o None para salir."""
    while True:
        print("\n╔══════════════════════════════╗")
        print("║     BIBLIOTECA MUSICAL       ║")
        print("╠══════════════════════════════╣")
        print("║  1. Iniciar sesión           ║")
        print("║  2. Crear nuevo usuario      ║")
        print("║  0. Salir                    ║")
        print("╚══════════════════════════════╝")
        op = input("Elige una opción: ").strip()

        if op == "0":
            return None

        elif op == "1":
            if not gestor._usuarios:
                print("No hay usuarios. Crea uno primero.")
                continue
            print("\nUsuarios disponibles:")
            for i, u in enumerate(gestor._usuarios, 1):
                print(f"  {i}. {u.nombre}  [{u.tipo_cuenta()}]")
            u = pedir_indice(gestor._usuarios, "Número de usuario: ")
            if u:
                print(f"\n¡Bienvenido/a, {u.nombre}! [{u.tipo_cuenta()}]")
                return u

        elif op == "2":
            u = formulario_nuevo_usuario(gestor)
            if u:
                gestor.agregar(u)
                gestor.guardar()
                gestor.guardar_pickle()
                print(f"Usuario '{u.nombre}' creado. ¡Bienvenido/a!")
                return u
        else:
            print("Opción no válida.")


def formulario_nuevo_usuario(gestor):
    """Pide los datos por consola y devuelve el nuevo usuario, o None si hay error."""
    print("\n--- Crear nuevo usuario ---")
    nombre = input("Nombre: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return None
    if gestor.existe(nombre):
        print(f"Ya existe un usuario llamado '{nombre}'.")
        return None

    email     = input("Email: ").strip()
    direccion = input("Dirección: ").strip()

    while True:
        try:
            edad = int(input("Edad: ").strip())
            if edad > 0:
                break
            print("La edad debe ser positiva.")
        except ValueError:
            print("Introduce un número entero.")

    print("\nTipos de cuenta disponibles:")
    tipos = list(TIPOS_USUARIO.keys())
    for i, t in enumerate(tipos, 1):
        print(f"  {i}. {t.capitalize()}")
    while True:
        try:
            tipo = tipos[int(input("Elige tipo: ").strip()) - 1]
            break
        except (ValueError, IndexError):
            print("Opción no válida.")

    return gestor.crear_usuario(nombre, email, edad, direccion, tipo)

# menu principal
def mostrar_menu(usuario):
    """
    Imprime dinámicamente las opciones disponibles

    Args:
        usuario: El usuario en sesión sobre el cual inspeccionar roles.
    """
    es_premium = isinstance(usuario, (UsuarioPremium, UsuarioSuper))
    es_admin   = isinstance(usuario, (UsuarioAdministrador, UsuarioSuper))

    print(f"\n=== MENÚ  [{usuario.nombre} · {usuario.tipo_cuenta()}] ===")
    print("=== Catálogo global ===")
    print("1.  Ver todas las pistas")
    print("2.  Buscar pistas")
    print("3.  Añadir pista al catálogo")
    print("4.  Reproducir una pista")
    print("=== Mis playlists ===")
    print("5.  Ver mis playlists")
    print("6.  Crear playlist")
    print("7.  Añadir pista a una playlist mía")
    print("8.  Reproducir una playlist mía")
    print("9.  Eliminar una playlist mía")
    if es_premium:
        print("=== Premium ===")
        print("10. Ver mis favoritos")
        print("11. Añadir pista a favoritos")
    if es_admin:
        print("=== Administración ===")
        print("12. Ver todos los usuarios")
        print("13. Eliminar pista del catálogo")
    print("======================================")
    print("14. Estadísticas")
    print("15. Cambiar de usuario")
    print("0.  Salir")

# acciones
def listar_pistas(biblioteca):
    """Muestra por consola la totalidad de pistas musicales indexadas en la biblioteca global."""
    if not biblioteca._pistas:
        print("No hay pistas en el catálogo.")
        return
    print("\nPistas en el catálogo:")
    for i, p in enumerate(biblioteca._pistas, 1):
        print(f"  {i}. {p}")


def buscar_pistas(biblioteca):
    """Busca las pistas aplicando filtros."""
    criterio = input("Buscar (título / artista / género): ").strip().lower()
    if not criterio:
        print("Escribe algo para buscar.")
        return
    resultados = []
    for p in biblioteca._pistas:
        if criterio in p.titulo.lower() or criterio in p.artista.lower() or criterio in str(p.genero).lower():
            resultados.append(p)
    if not resultados:
        print("Sin resultados.")
    else:
        for p in resultados:
            print(f"  {p}")


def anadir_pista_catalogo(biblioteca):
    """Solicita los datos requeridos e añade una nueva pista"""
    try:
        titulo  = input("Título: ").strip()
        artista = input("Artista: ").strip()
        assert titulo,  "El título no puede estar vacío."
        assert artista, "El artista no puede estar vacío."
        nueva = Pista(titulo, artista, pedir_genero(), pedir_duracion())
        biblioteca.agregar_pista(nueva)
        biblioteca.guardar_csv()
        print(f"Pista '{titulo}' añadida al catálogo.")
    except AssertionError as e:
        print(f"Error: {e}")


def reproducir_pista(biblioteca):
    """Permite seleccionar una pista del catálogo y procesa su simulación."""
    if not biblioteca._pistas:
        print("No hay pistas.")
        return
    listar_pistas(biblioteca)
    p = pedir_indice(biblioteca._pistas, "Número de pista: ")
    if p:
        print("\n▶ Reproduciendo...")
        p.reproducir()
        minutos = p.duracion // 60
        segundos = p.duracion % 60
        print(f"   Duración: {minutos}:{segundos:02d} min")
        print("- Reproducción finalizada.")


def listar_mis_playlists(usuario):
    """Imprime playlists personales vinculadas al usuario."""
    if not usuario._playlists:
        print("No tienes playlists.")
        return
    print(f"\nPlaylists de {usuario.nombre}:")
    for i, pl in enumerate(usuario._playlists, 1):
        print(f"  {i}. {pl}")


def crear_playlist(usuario, gestor, biblioteca):
    """Inicializa una nueva lista vacía delegando en el usuario para verificar restricciones de cuota."""
    nombre = input("Nombre de la playlist: ").strip()
    estado = input("Estado de ánimo: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return
    try:
        pl = Playlist(nombre, estado)
        usuario.crear_playlist(pl)   # UsuarioGratis aplica su límite aquí
        gestor.guardar_playlists_usuario(usuario)
        print(f"Playlist '{nombre}' creada.")
    except ValueError as e:
        print(f"No se pudo crear: {e}")


def anadir_pista_a_playlist(usuario, gestor, biblioteca):
    """Vincula una de las canciones disponibles en el catálogo general dentro de una playlist propia."""
    if not biblioteca._pistas:
        print("No hay pistas en el catálogo.")
        return
    if not usuario._playlists:
        print("No tienes playlists. Crea una primero.")
        return
    listar_pistas(biblioteca)
    pista = pedir_indice(biblioteca._pistas, "Número de pista: ")
    if not pista:
        return
    listar_mis_playlists(usuario)
    pl = pedir_indice(usuario._playlists, "Número de playlist: ")
    if not pl:
        return
    pl.agregar_pista(pista)
    gestor.guardar_playlists_usuario(usuario)
    print(f"'{pista.titulo}' añadida a '{pl.titulo}'.")


def reproducir_playlist(usuario):
    """Desencadena la reproducción en secuencia de todas las pistas anexadas a la playlist elegida."""
    if not usuario._playlists:
        print("No tienes playlists.")
        return
    listar_mis_playlists(usuario)
    pl = pedir_indice(usuario._playlists, "Número de playlist: ")
    if pl:
        if not pl._pistas:
            print("Esta playlist no tiene pistas.")
            return
        print(f"\n- Reproduciendo playlist: {pl.titulo} ({pl.estado_animo})")
        print(f"   {len(pl._pistas)} pista(s) en cola\n")
        for i, p in enumerate(pl._pistas, 1):
            print(f"   {i}. ", end="")
            p.reproducir()
        print("■ Playlist finalizada.")


def eliminar_playlist(usuario, gestor, biblioteca):
    """Elimina irreversiblemente una playlist del usuario activo."""
    if not usuario._playlists:
        print("No tienes playlists.")
        return
    listar_mis_playlists(usuario)
    pl = pedir_indice(usuario._playlists, "Número a eliminar: ")
    if not pl:
        return
    confirmacion = input(f"¿Eliminar '{pl.titulo}'? (s/n): ").strip().lower()
    if confirmacion == "s":
        usuario.eliminar_playlist(pl)
        gestor.guardar_playlists_usuario(usuario)
        gestor.guardar()
        gestor.guardar_pickle()
        print("Playlist eliminada.")


def ver_favoritos(usuario):
    """Lista las canciones marcadas (Solo cuentas Premium/Super)."""
    if not usuario._favoritos:
        print("No tienes favoritos.")
    else:
        print("Tus favoritos:")
        for p in usuario._favoritos:
            print(f"  {p}")


def anadir_favorito(usuario, biblioteca):
    """Añade una pista en la colección de favoritos del usuario (Solo cuentas Premium/Super)."""
    listar_pistas(biblioteca)
    p = pedir_indice(biblioteca._pistas, "Número de pista: ")
    if p:
        usuario.agregar_a_favoritos(p)
        print(f"'{p.titulo}' añadida a favoritos.")


def ver_todos_usuarios(gestor):
    """información de todas las cuentas creadas (Solo Administradores)."""
    print("\nUsuarios registrados:")
    for u in gestor._usuarios:
        print(f"  {u.nombre} | {u.email} | {u.tipo_cuenta()} | {len(u._playlists)} playlist(s)")


def eliminar_pista_catalogo(biblioteca):
    """Borra de forma definitiva una pista musical del catálogo maestro y sus playlists (Solo Administradores)."""
    if not biblioteca._pistas:
        print("No hay pistas.")
        return
    listar_pistas(biblioteca)
    p = pedir_indice(biblioteca._pistas, "Número a eliminar: ")
    if not p:
        return
    confirmacion = input(f"¿Eliminar '{p.titulo}' del catálogo? (s/n): ").strip().lower()
    if confirmacion == "s":
        biblioteca.eliminar_pista(p)
        biblioteca.guardar_csv()
        print("Pista eliminada del catálogo.")


def mostrar_estadisticas(usuario, biblioteca):
    """Calcula y muestra métricas globales, acumulando tiempos globales de las canciones del sistema."""
    duracion_total = 0
    for p in biblioteca._pistas:
        duracion_total += p.duracion
    print(f"\n  Pistas en catálogo : {len(biblioteca._pistas)}")
    print(f"  Playlists globales : {len(biblioteca._playlists)}")
    print(f"  Mis playlists      : {len(usuario._playlists)}")
    print(f"  Duración catálogo  : {duracion_total}s ({duracion_total // 60} min)")


def bucle_sesion(usuario, gestor, biblioteca):
    """
    Bucle de menú para el usuario activo.
    Devuelve True si hay que volver al login, False si hay que salir.
    """
    gestor.cargar_playlists_usuario(usuario, biblioteca)
    es_premium = isinstance(usuario, (UsuarioPremium, UsuarioSuper))
    es_admin   = isinstance(usuario, (UsuarioAdministrador, UsuarioSuper))

    while True:
        mostrar_menu(usuario)
        op = input("Elige una opción: ").strip()

        if   op == "1":  listar_pistas(biblioteca)
        elif op == "2":  buscar_pistas(biblioteca)
        elif op == "3":  anadir_pista_catalogo(biblioteca)
        elif op == "4":  reproducir_pista(biblioteca)
        elif op == "5":  listar_mis_playlists(usuario)
        elif op == "6":  crear_playlist(usuario, gestor, biblioteca)
        elif op == "7":  anadir_pista_a_playlist(usuario, gestor, biblioteca)
        elif op == "8":  reproducir_playlist(usuario)
        elif op == "9":  eliminar_playlist(usuario, gestor, biblioteca)
        elif op == "10":
            if es_premium: ver_favoritos(usuario)
            else: print("Solo disponible para cuentas Premium o Super.")
        elif op == "11":
            if es_premium: anadir_favorito(usuario, biblioteca)
            else: print("Solo disponible para cuentas Premium o Super.")
        elif op == "12":
            if es_admin: ver_todos_usuarios(gestor)
            else: print("Solo disponible para Administrador o Super.")
        elif op == "13":
            if es_admin: eliminar_pista_catalogo(biblioteca)
            else: print("Solo disponible para Administrador o Super.")
        elif op == "14": mostrar_estadisticas(usuario, biblioteca)
        elif op == "15":
            gestor.guardar_playlists_usuario(usuario)
            return True
        elif op == "0":
            gestor.guardar_playlists_usuario(usuario)
            return False
        else:
            print("Opción no válida.")


# main
def main():
    # Cargar biblioteca global
    biblioteca = Biblioteca()
    biblioteca.cargar_csv()
    if not biblioteca._pistas and not biblioteca._playlists:
        crear_datos_ejemplo(biblioteca)
        biblioteca.guardar_csv()

    # Cargar usuarios — primero intenta pickle, si no hay carga el CSV
    gestor = GestorUsuarios(CARPETA_DATOS)
    gestor.cargar_pickle()
    if not gestor._usuarios:
        gestor.cargar()
    if not gestor._usuarios:
        crear_usuarios_ejemplo(gestor)

    # Bucle de sesiones (permite cambiar de usuario sin salir)
    while True:
        usuario = pantalla_login(gestor)
        if usuario is None:
            biblioteca.guardar_csv()
            gestor.guardar()
            gestor.guardar_pickle()
            print("¡Hasta pronto!")
            break

        cambiar_usuario = bucle_sesion(usuario, gestor, biblioteca)
        if not cambiar_usuario:
            biblioteca.guardar_csv()
            gestor.guardar()
            gestor.guardar_pickle()
            print("¡Hasta pronto!")
            break


if __name__ == "__main__":
    main()
