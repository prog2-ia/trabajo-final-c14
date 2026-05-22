import csv
import os
from usuarios.usuario_gratis import UsuarioGratis
from usuarios.usuario_premium import UsuarioPremium
from usuarios.usuario_administrador import UsuarioAdministrador
from usuarios.usuario_super import UsuarioSuper
from playlist.playlist import Playlist
from servicios.pickle_manager import PickleManager
from excepciones.excepciones import UsuarioYaExisteError, UsuarioNoEncontradoError

# Diccionario para convertir entre el string del CSV y la clase correspondiente
TIPOS_USUARIO = {
    "gratis":        UsuarioGratis,
    "premium":       UsuarioPremium,
    "administrador": UsuarioAdministrador,
    "super":         UsuarioSuper,
}


class GestorUsuarios:
    """
    Gestiona la lista de usuarios y su persistencia en CSV.
    Preparado para que en el futuro se pueda añadir pickle
    creando una subclase que sobreescriba guardar() y cargar().
    """

    def __init__(self, carpeta_datos):
        self._carpeta = carpeta_datos
        os.makedirs(self._carpeta, exist_ok=True)
        self._usuarios = []
        self._pickle = PickleManager(os.path.join(carpeta_datos, "usuarios.pkl"))

    #  Rutas 

    def _ruta(self, nombre_archivo):
        """Devuelve la ruta completa de un archivo dentro de la carpeta de datos."""
        return os.path.join(self._carpeta, nombre_archivo)

    def _ruta_playlists(self, usuario):
        """Devuelve la ruta del CSV de playlists de un usuario."""
        nombre_seguro = usuario.nombre.lower().replace(" ", "_")
        return self._ruta(f"playlists_{nombre_seguro}.csv")

    # Usuarios 

    def guardar(self):
        """Guarda todos los usuarios en usuarios.csv."""
        ruta = self._ruta("usuarios.csv")
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["nombre", "email", "edad", "direccion", "tipo"])
            writer.writeheader()
            for u in self._usuarios:
                # Averiguamos el tipo del usuario comparando con el diccionario
                tipo = "gratis"
                for clave, clase in TIPOS_USUARIO.items():
                    if type(u) is clase:
                        tipo = clave
                        break
                writer.writerow({
                    "nombre":    u.nombre,
                    "email":     u.email,
                    "edad":      u.edad,
                    "direccion": u.direccion,
                    "tipo":      tipo,
                })

    def cargar(self):
        """Carga los usuarios desde usuarios.csv."""
        ruta = self._ruta("usuarios.csv")
        self._usuarios = []
        if not os.path.exists(ruta):
            return
        with open(ruta, newline="", encoding="utf-8") as f:
            for fila in csv.DictReader(f):
                clase = TIPOS_USUARIO.get(fila["tipo"], UsuarioGratis)
                u = clase(fila["nombre"], fila["email"], int(fila["edad"]), fila["direccion"])
                self._usuarios.append(u)

    def agregar(self, usuario):
        """Añade un usuario a la lista en memoria."""
        self._usuarios.append(usuario)

    def existe(self, nombre):
        """Comprueba si ya existe un usuario con ese nombre."""
        for u in self._usuarios:
            if u.nombre.lower() == nombre.lower():
                return True
        return False

    def crear_usuario(self, nombre, email, edad, direccion, tipo):
        """Crea y devuelve un usuario del tipo indicado."""
        clase = TIPOS_USUARIO.get(tipo, UsuarioGratis)
        return clase(nombre, email, edad, direccion)

    # Playlists por usuario 
    def guardar_playlists_usuario(self, usuario):
        """Guarda las playlists de un usuario en su CSV individual."""
        ruta = self._ruta_playlists(usuario)
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["titulo", "estado_animo", "pistas"])
            writer.writeheader()
            for pl in usuario._playlists:
                pistas_txt = "|".join(p.titulo for p in pl._pistas)
                writer.writerow({
                    "titulo":       pl.titulo,
                    "estado_animo": pl.estado_animo,
                    "pistas":       pistas_txt,
                })

    def cargar_playlists_usuario(self, usuario, biblioteca):
        """Carga las playlists de un usuario desde su CSV."""
        ruta = self._ruta_playlists(usuario)
        if not os.path.exists(ruta):
            return
        # Índice título->pista para enlazar las pistas de la biblioteca
        pistas_por_titulo = {}
        for p in biblioteca._pistas:
            pistas_por_titulo[p.titulo] = p

        usuario._playlists = []
        with open(ruta, newline="", encoding="utf-8") as f:
            for fila in csv.DictReader(f):
                pl = Playlist(fila["titulo"], fila["estado_animo"])
                for titulo in fila["pistas"].split("|"):
                    titulo = titulo.strip()
                    if titulo in pistas_por_titulo:
                        pl.agregar_pista(pistas_por_titulo[titulo])
                usuario._playlists.append(pl)

    # pickle 
    def guardar_pickle(self):
        """Serializa la lista completa de usuarios en un archivo binario .pkl."""
        self._pickle.guardar(self._usuarios)
 
    def cargar_pickle(self):
        """Carga los usuarios desde el archivo .pkl (si existe) y los pone en memoria."""
        cargados = self._pickle.cargar()
        if cargados:
            self._usuarios = cargados
 
    def crear_usuario(self, nombre, email, edad, direccion, tipo):
        """Crea y devuelve un usuario del tipo indicado."""
        clase = TIPOS_USUARIO.get(tipo, UsuarioGratis)
        return clase(nombre, email, edad, direccion)
 
    # Playlists por usuario 
    def guardar_playlists_usuario(self, usuario):
        """Guarda las playlists de un usuario en su CSV individual."""
        ruta = self._ruta_playlists(usuario)
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["titulo", "estado_animo", "pistas"])
            writer.writeheader()
            for pl in usuario._playlists:
                pistas_txt = "|".join(p.titulo for p in pl._pistas)
                writer.writerow({
                    "titulo":       pl.titulo,
                    "estado_animo": pl.estado_animo,
                    "pistas":       pistas_txt,
                })
 
    def cargar_playlists_usuario(self, usuario, biblioteca):
        """Carga las playlists de un usuario desde su CSV."""
        ruta = self._ruta_playlists(usuario)
        if not os.path.exists(ruta):
            return
        # Índice título->pista para enlazar las pistas de la biblioteca
        pistas_por_titulo = {}
        for p in biblioteca._pistas:
            pistas_por_titulo[p.titulo] = p
 
        usuario._playlists = []
        with open(ruta, newline="", encoding="utf-8") as f:
            for fila in csv.DictReader(f):
                pl = Playlist(fila["titulo"], fila["estado_animo"])
                for titulo in fila["pistas"].split("|"):
                    titulo = titulo.strip()
                    if titulo in pistas_por_titulo:
                        pl.agregar_pista(pistas_por_titulo[titulo])
                usuario._playlists.append(pl)