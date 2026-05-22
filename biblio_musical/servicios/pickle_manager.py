import pickle
import os
from excepciones.excepciones import PersistenciaError


class PickleManager:
    """Gestiona la serialización y deserialización binaria de la lista de usuarios."""

    def __init__(self, ruta: str):
        self._ruta = ruta
        os.makedirs(os.path.dirname(ruta), exist_ok=True)

    # Guardar

    def guardar(self, usuarios: list) -> None:
        """
        Serializa la lista de usuarios en el archivo .pkl.
        """
        try:
            with open(self._ruta, "wb") as f:   # "wb" = write binary
                pickle.dump(usuarios, f)
            print(f"[Pickle] {len(usuarios)} usuarios guardados en '{self._ruta}'.")
        except OSError as e:
            raise PersistenciaError(self._ruta, "escribir") from e

    # Cargar

    def cargar(self) -> list:
        """
        Deserializa el archivo .pkl y devuelve la lista de usuarios.
        """
        if not os.path.exists(self._ruta):
            return []
        try:
            with open(self._ruta, "rb") as f:   # "rb" = read binary
                usuarios = pickle.load(f)
            print(f"[Pickle] {len(usuarios)} usuarios cargados desde '{self._ruta}'.")
            return usuarios
        except (OSError, pickle.UnpicklingError) as e:
            raise PersistenciaError(self._ruta, "leer") from e

    # Utilidades

    def existe(self) -> bool:
        """Comprueba si ya existe un archivo pickle guardado."""
        return os.path.exists(self._ruta)

    def eliminar(self) -> None:
        """
        Borra el archivo pickle si existe.
        """
        if not self.existe():
            return
        try:
            os.remove(self._ruta)
            print(f"[Pickle] Archivo '{self._ruta}' eliminado.")
        except OSError as e:
            raise PersistenciaError(self._ruta, "eliminar") from e

    def __repr__(self):
        return f"PickleManager(ruta='{self._ruta}', existe={self.existe()})"