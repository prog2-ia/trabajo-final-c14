from servicios.csv_manager import leer_csv, escribir_csv 
from contenido.genero import Genero
from contenido.pista import Pista
from playlist.playlist import Playlist

class Biblioteca:

    """Gestiona todas las pistas y playlists del sistema."""

    def __init__(self) -> None:
        self._pistas = []
        self._playlists = []

    def agregar_pista(self, pista)-> None:
        """Añade una pista a la biblioteca."""
        self._pistas.append(pista)

    def crear_playlist(self, playlist):
        """Añade una playlist."""
        self._playlists.append(playlist)

    def reproducir_todo(self) -> None:
        """Reproduce todo el contenido."""
        print(" Reproduciendo toda la biblioteca")
        for p in self._pistas:
            p.reproducir()

        for pl in self._playlists:
            pl.reproducir()

    def buscar(self, genero=None, artista=None, max_duracion=None,estado_animo=None, calidad=None) -> list:
        resultados = self._pistas
        if genero is not None:
            resultados = [p for p in resultados
                          if p._genero.nombre.lower() == genero.lower()]
        if artista is not None:
            resultados = [p for p in resultados
                          if p._artista.lower() == artista.lower()]
        if max_duracion is not None:
            resultados = [p for p in resultados
                          if p._duracion <= max_duracion]
        if estado_animo is not None:
            resultados = [p for p in resultados
                          if p._estado_animo and p._estado_animo.lower() == estado_animo.lower()]
        if calidad is not None:
            resultados = [p for p in resultados
                          if p._calidad and p._calidad.lower() == calidad.lower()]

        return resultados
    
    def eliminar_pista(self, pista) -> bool:
        """Elimina una pista de la biblioteca y de todas las playlists donde aparezca."""
        if pista not in self._pistas:
            return False
        self._pistas.remove(pista)
        for playlist in self._playlists:
            if pista in playlist._pistas:
                playlist.eliminar_pista(pista)
        return True   
    
    def eliminar_playlist(self, playlist) -> bool:
        """Elimina una playlist de la biblioteca."""
        if playlist not in self._playlists:
            return False
        self._playlists.remove(playlist)
        return True

    def guardar_pistas_csv(self):
        """Guarda todas las pistas en datos/pistas.csv."""
        filas = []
        for pista in self._pistas:
            filas.append({
                "titulo": pista.titulo,
                "artista": pista.artista,
                "genero": str(pista.genero),
                "duracion": pista.duracion,
            })
        escribir_csv("pistas.csv", filas, ["titulo", "artista", "genero", "duracion"])

    def cargar_pistas_csv(self):
        """Carga las pistas desde datos/pistas.csv."""
        filas = leer_csv("pistas.csv")
        self._pistas = []
        for fila in filas:
            if not fila.get("titulo") or not fila.get("artista"):
                continue
            genero = Genero(fila.get("genero", "Desconocido"))
            duracion = int(fila.get("duracion", 0)) if fila.get("duracion") else 0
            pista = Pista(fila["titulo"], fila["artista"], genero, duracion)
            self._pistas.append(pista)

    def guardar_playlists_csv(self):
        """Guarda las playlists en datos/playlists.csv."""
        filas = []
        for playlist in self._playlists:
            pistas_texto = "|".join(p.titulo for p in getattr(playlist, "_pistas", []))
            filas.append({
                "titulo": playlist.titulo,
                "estado_animo": getattr(playlist, "estado_animo", ""),
                "pistas": pistas_texto,
            })
        escribir_csv("playlists.csv", filas, ["titulo", "estado_animo", "pistas"])

    def cargar_playlists_csv(self):
        """Carga las playlists desde datos/playlists.csv."""
        filas = leer_csv("playlists.csv")
        self._playlists = []
        pistas_por_titulo = {p.titulo: p for p in self._pistas}
        for fila in filas:
            if not fila.get("titulo"):
                continue
            playlist = Playlist(fila["titulo"], fila.get("estado_animo", ""))
            for titulo_pista in fila.get("pistas", "").split("|"):
                titulo_pista = titulo_pista.strip()
                if titulo_pista and titulo_pista in pistas_por_titulo:
                    playlist.agregar_pista(pistas_por_titulo[titulo_pista])
            self._playlists.append(playlist)

    def guardar_csv(self):
        """Guarda pistas y playlists en CSV."""
        self.guardar_pistas_csv()
        self.guardar_playlists_csv()

    def cargar_csv(self):
        """Carga pistas y playlists desde CSV."""
        self.cargar_pistas_csv()
        self.cargar_playlists_csv()


    def __str__(self):
        return f"Biblioteca: {len(self._pistas)} pistas, {len(self._playlists)} playlists"

    def __repr__(self):
        return f"Biblioteca(pistas={len(self._pistas)}, playlists={len(self._playlists)})"