""" Representa un género musical, como Rock, Pop, Jazz... """
class Genero:
    def __init__(self, nombre):
        """ Inicializa el género
            Si nombre es una cadena no vacía, se guarda con la primera letra en mayúscula
            Si no, se asigna "Desconocido """
        if isinstance(nombre, str) and nombre.strip():
            self.nombre = nombre.strip().title()  # Eliminamos espacios y capitalizamos
        else:
            self.nombre = "Desconocido"

    def descripcion(self):
        """ Devuelve una descripción amigable del género """
        return f"Género musical: {self.nombre}"

    def __str__(self):
        """ Método para representar el género como cadena (por ejemplo al imprimir) """
        return self.nombre

    def __repr__(self):
        """ Representación oficial del objeto, útil para depuración """
        return f"Genero('{self.nombre}')"
