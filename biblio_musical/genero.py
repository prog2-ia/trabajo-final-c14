class Genero:
    def __init__(self, nombre):
        if isinstance(nombre, str) and nombre.strip():
            self.nombre = nombre.strip().title()
        else:
            self.nombre = "Desconocido"

    def descripcion(self):
        return f"Género musical: {self.nombre}"

    def __str__(self):
        return self.nombre

    def __repr__(self):
        return f"Genero('{self.nombre}')"
